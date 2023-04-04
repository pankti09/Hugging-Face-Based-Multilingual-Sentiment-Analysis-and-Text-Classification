from flask import Flask, request, jsonify
import numpy as np
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline
import os

app = Flask(__name__)

# The model prediction
model_path = './que2_model/transformers/' 
model = TFAutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# Flask deployment 
@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        results = classifier(data)
        return jsonify(results)
    return 'Hi! Data is to be transmitted.'

if __name__ == '__main__':
    # Socket deployment
    sock = f"/tmp/gunicorn.sock"
    os.environ['PORT'] = sock
    command = f"gunicorn app:app --bind unix:{sock} --workers 4"
    os.system(command)


    '''To prevent having to refresh the model and tokenizer for each request, we load them again outside of the Flask endpoint.

Afterwards, we create a Unix domain socket for NGINX and the Flask application to communicate with one another. In order for Gunicorn to bind to the socket, we set the PORT environment variable to the route. Also, we set up Gunicorn so that it uses 4 worker processes to deal with incoming requests.


The command variable, which contains the name of the Flask app (app), the socket path (sock), and the number of workers, is then used to launch Gunicorn using the os.system() function (4). NGINX must be set up to forward requests to the socket as well. This is a sample NGINX configuration file:

Config file 
    
    
    server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://unix:/tmp/gunicorn.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}'''