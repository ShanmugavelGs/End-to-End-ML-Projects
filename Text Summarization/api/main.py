import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from transformers import pipeline
import textwrap

CREATE_INPUT_TABLE = (
"CREATE TABLE IF NOT EXISTS userInput (id SERIAL PRIMARY KEY, paragraph TEXT NOT NULL);"
)

CREATE_OUTPUT_TABLE = (
    "CREATE TABLE IF NOT EXISTS userOutput (id SERIAL PRIMARY KEY, "
    "userInputID INTEGER REFERENCES userInput(id), summarizedText TEXT NOT NULL);"
)

load_dotenv()

app = Flask(__name__)
url = os.environ.get("DATABASE_URL")
connection = psycopg2.connect(url)

summarizer = pipeline("summarization", model="D:\Project Files\Hugging Face\Text Summarization\model")

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()

    if 'paragraph' not in data:
        return jsonify({'error': 'Missing paragraph field in JSON data'}), 400

    paragraph = data['paragraph']

    with connection:
        with connection.cursor() as cursor:
            # Create userOutput table if not exists
            cursor.execute(CREATE_INPUT_TABLE)
            cursor.execute(CREATE_OUTPUT_TABLE)

             # Insert user input into userInput table
            insert_query = "INSERT INTO userInput (paragraph) VALUES (%s) RETURNING id"
            cursor.execute(insert_query, (paragraph,))
            userInputID = cursor.fetchone()[0]
           

            # Perform summarization on the fetched paragraph
            wrapped_text = summarizer(paragraph, max_length=200, min_length=30, do_sample=False)
            summary = [textwrap.fill(text['summary_text'], width=90) for text in wrapped_text]

            # Insert summarized output into userOutput table
            insert_query = "INSERT INTO userOutput (userInputID, summarizedText) VALUES (%s, %s)"
            cursor.execute(insert_query, (userInputID, summary))

    return jsonify({'userInputID': userInputID, 'summary': summary}), 201


if __name__ == "__main__":
    app.run(debug=True)