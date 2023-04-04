# Lemay.ai-Assessment

The repository contains the Que 2 and Que 3 of the assessment. 
In the Que2, the model is uploaded here, https://drive.google.com/drive/folders/1rdfV563J_Je00_RWojN5cwRcSsbGRyam?usp=sharing.

The model can be downloaded from the gdrive link mentioned here. A transformer-based language model that has already been trained for sentiment analysis tasks is nlptown/bert-base-multilingual-uncased-sentiment. It has been trained on a sizable corpus of text in numerous languages and is based on the BERT (Bidirectional Encoder Representations from Transformers) architecture. Using a piece of text as input, the model generates a sentiment score between 0 and 1, with 0 denoting a negative sentiment and 1 denoting a good sentiment. The model is a helpful tool for sentiment analysis jobs in multilingual environments since it can handle text in a variety of languages.The Hugging Face Transformers package, which offers a simple Python API for loading and using pre-trained transformer models, makes this model usable. 

**This model was chosen due to BERT-based architecture because: The widely-used BERT architecture, which is built on transformers, has produced cutting-edge results for a variety of sentiment analysis applications in natural language processing. For sentiment analysis tasks, a BERT-based model can be an excellent place to start. The Hugging Face Transformers package, which offers a simple Python API for loading and using pre-trained transformer models, makes the model available. This can make integrating the model into an already-existing sentiment analysis process simple.**

In order to run the model on docker, following commands has to be used. 

First, we need to have flask. We need to **set FLASK_APP=app.py**. We can run it by **flask run** or **python -m flask run**.
Secondly, we need to create a docker image **docker build — tag lemaynlp .**. Then,we need to create the docker image and container by selecting respective port number **docker run -i -p 6000:8000 lemaynlp**.
In order to check, whether its recieving properly we can run **curl //localhost:9000 -v**. Now, we can check all running containers in **docker ps**
Here, in Que 3, **the dataset ag_news was selected.** As discussed in the meeting, the task is related to medical device mainly. Thus, I thought of taking this dataset. For text classification tasks, a collection of news stories known as the AG News dataset has been extensively employed. It includes 120,000 news items from the World, Sports, Business, and Science/Technology categories. The dataset was first developed to assess the performance of several machine learning algorithms for text categorization tasks.The news pieces came from the English-language editions of a number of news organisations, including CNN, Reuters, and the BBC. Each piece of content in the dataset is assigned to one of the four aforementioned groups. With 30,000 articles in each of the four categories, the dataset is uniformly distributed. We can use this pre-processing as a reference for fetching the data from the mdeical reports or articles. 

The file Pankti_Lemay_ai_que3.ipynb contains the details about the que3. 
