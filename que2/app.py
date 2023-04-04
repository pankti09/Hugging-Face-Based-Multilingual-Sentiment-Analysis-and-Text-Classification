from flask import Flask, request, jsonify
import numpy as np
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline

app = Flask(__name__)

#Flask deployment 
@app.route('/', methods=['GET', 'POST'])
def mmakex():
    if request.method=="POST":
        data = request.get_json()
        print("data ---- > ", data)
        results = classifier(data)
        
        return jsonify(results)
    return "Hi! Data is to be transmitted."

#the model prediction

#The basic prediction of model 
if __name__ == '__main__':

    model_path = './que2_model/transformers/' 
    model = TFAutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
    print(classifier)

    app.run()

