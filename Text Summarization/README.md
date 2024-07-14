# Text Summarization using NLP Pretrained Transformer from Hugging Face Using `facebook/bart-large-cnn`

This project is a complete end-to-end machine learning solution utilizing a pretrained transformer model from Hugging Face. Specifically, the `facebook/bart-large-cnn` model is used for text summarization. The project involves the following components:

- **Flask API**: A Flask application is used to create API endpoints that handle POST requests for text summarization.
- **PostgreSQL**: PostgreSQL serves as the relational database management system (RDBMS) to store and manage user data.
- **Streamlit**: Streamlit is employed to design a user-friendly UI for interacting with the text summarization model.
- **Docker** (optional): The project can be containerized using Docker to facilitate localization and deployment.

This project demonstrates the integration of advanced NLP models with practical application development tools, providing a robust solution for text summarization tasks.


## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ShanmugavelGs/End-to-End-Projects.git

2. Create the test environment using Anaconda Prompt
   
   conda create -n test_env
   conda install pip

3. Install the dependencies

   pip install -r requirements.txt

4. Create a .env file and enter the database URL

   DATABASE_URL=postgresql://username:password@localhost:5432/dbname

5. Change the directory of your model folder and run the model file

   summarizer.save_pretrained('change the dir here, to your model file')

   python model.py

6. Change the model directory in main.py file

   summarizer = pipeline("summarization", model="change the dir here, to your model file")

## Usage

1. Start the Flask AP

   python main.py

2. Open Streamlit UI

   streamlit run summarizer.py

3. After the first use, check for user input and output table in your db 

