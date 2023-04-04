#This file will download all the dependent files



from transformers import pipeline
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification    
model_path = 'que2_model/transformers/'

#%%themodel files will be saved in the specific folder
#%% download and save the model to local directory, The reference was taken from the hugging face model hub
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

model = TFAutoModelForSequenceClassification.from_pretrained(model_name, from_pt=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
classifier.save_pretrained(model_path)

#%% Loading the model from the directory to 
model = TFAutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

classifier(["good"]) 

