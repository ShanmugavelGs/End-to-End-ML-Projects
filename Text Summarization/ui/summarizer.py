import streamlit as st
import requests
import json

# Define the API URL based on Docker service name/localhost
API_URL = "http://localhost:5000/summarize"

def main():
    st.title("Summarizer App")
    paragraph = st.text_area("Enter the paragraph you want to summarize", height=200)

    # Button to trigger summarization
    if st.button("Summarize"):
        if paragraph:
            # Prepare data for POST request
            input_data = {"paragraph": paragraph}
        
            # Send POST request to Flask API
            response = requests.post(url="http://localhost:5000/summarize", data=json.dumps(input_data), headers={"Content-Type": "application/json"})
        
            # Parse response from Flask API
            if response.status_code == 201:
                summary = response.json().get('summary', 'No summary returned')
                st.subheader("Summarized Text")
                st.write(summary[0])
            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error occurred')}")
    else:
        st.error("Please enter a paragraph to summarize.")

if __name__=='__main__':
    main()