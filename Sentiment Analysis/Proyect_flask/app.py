from flask import Flask, render_template, request
import keras
from keras.preprocessing.sequence import pad_sequences
from keras_preprocessing.text import tokenizer_from_json
import json
import re
import pickle


app = Flask(__name__)


def treatment(text):
    
    #Remove accents
    a,b = 'áéíóúüÁÉÍÓÚÜ','aeiouuAEIOUU'
    trans = str.maketrans(a,b)
    text = text.translate(trans)
    
    #Remove line breaks and tabs
    text = re.sub("[\n,\t]", ' ', text)
    
    #Remove tags, links and numbers
    text = re.sub("(@[A-Za-z0-9\_\-\.]+)|(\w+:\/\/\S+)|(\d+[\w+\-\/]*)|(www\.\S+)", '', text)

    #Remove special characters
    text = re.sub("[#,&,$,!,',),(,-,*,;,:,|,\",.,?,¿,¡]", '', text)

    #Remove emojies
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
                    "]+", re.UNICODE)
    text = re.sub(emoj, '', text)    
        
    #Remove spaces at the beginning and end
    text = text.strip()
    
    #Transform to lowercase
    text = text.lower()
    
    # Remove stopwords
    with open("stopwords.pickle", "rb") as f:
        stop_words = pickle.load(f)
    text = ' '.join([word for word in text.split() if word not in stop_words])

    return text


def evaluation(text):
    
    clean_text = treatment(text)
        
    # Change texts into sequence of indexes
    with open('tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    X = tokenizer.texts_to_sequences([clean_text]) #Change the texts into numeric identifiers that represent the index of each word in the dictionary

    # Pad the sequences
    X = pad_sequences(X, 40) #Sequences have the same size
    
    #Change input form
    X_ = X.reshape(X.shape[0],X.shape[1],1)
    
    #Model loaded
    model = keras.models.load_model('best_model.hdf5')
    
    predictions = model.predict(X_).reshape(1,-1)[0]
    predictions = ["Positivo" if x < 0.5 else "Negativo" for x in predictions]
    
    return (clean_text, predictions[0])


@app.route('/', methods=['GET', 'POST'])
def index():
    result=""
    if request.method == "POST":
        text = request.form['text']
        clean_text, value = evaluation(text)
        result = [text, clean_text, value]
    return render_template('home.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


