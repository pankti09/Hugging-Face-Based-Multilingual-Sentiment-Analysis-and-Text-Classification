# Hugging Face-Based Multilingual Sentiment Analysis and Text Classification

This repository contains the work related to sentiment analysis and text classification using transformer-based models.

In the first part of the project, the pre-trained model nlptown/bert-base-multilingual-uncased-sentiment is used for sentiment analysis tasks. This model, built on the BERT (Bidirectional Encoder Representations from Transformers) architecture, has been trained on a sizable corpus of text in numerous languages. Given a piece of text as input, it generates a sentiment score between 0 and 1, with 0 indicating negative sentiment and 1 indicating positive sentiment. The model is particularly useful for sentiment analysis in multilingual environments as it can handle text in various languages. The Hugging Face Transformers package provides a simple Python API for loading and using this pre-trained model.

**Why Use a BERT-Based Model?**
The BERT architecture, based on transformers, has produced state-of-the-art results for various sentiment analysis tasks in natural language processing. The Hugging Face Transformers package simplifies the integration of this model into existing sentiment analysis processes, making it an excellent starting point for such tasks.

To run the model on Docker, follow these steps:

Install Flask and set up the environment: **set FLASK_APP=app.py**. Run it with flask run or python -m flask run.
Create a Docker image: **docker build — tag nlp** ..
Create a Docker container and specify the port: **docker run -i -p 6000:8000 nlp**
Check if the container is receiving properly using **curl //localhost:9000 -v**
View all running containers with **docker ps**.
Test the output by running test.py. The test output is available in the project folder.
For handling parallel requests and POST operations, refer to the code in **app_nginx**.py.
In the second part of the project, the AG News dataset was selected for text classification tasks. The task relates to the classification of news articles, with a potential application in the medical domain. The AG News dataset consists of 120,000 news articles categorized into four groups: World, Sports, Business, and Science/Technology. It has been widely used to evaluate the performance of machine learning algorithms for text categorization. The dataset includes articles from various news organizations, such as CNN, Reuters, and the BBC, with 30,000 articles in each category, making it evenly distributed. The pre-processing steps can serve as a reference for fetching data from medical reports or articles.

Details for this part of the project are available in the file main.ipynb.
