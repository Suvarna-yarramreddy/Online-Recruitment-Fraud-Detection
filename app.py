#=================flask code starts here
from flask import Flask, render_template, request, redirect, url_for, session,send_from_directory
import os
from werkzeug.utils import secure_filename
from distutils.log import debug
from fileinput import filename
from datetime import datetime
from werkzeug.utils import secure_filename
import sqlite3
import pickle
import sqlite3

import numpy as np
import pandas as pd
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt   
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer #loading bert sentence model
from string import punctuation
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
from nltk.stem import PorterStemmer
import smote_variants
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.layers import  MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D
from keras.models import Sequential, load_model, Model
import pickle
from sklearn.metrics import accuracy_score
from keras.callbacks import ModelCheckpoint
import os


UPLOAD_FOLDER = os.path.join('static', 'uploads') 
# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'welcome'

berts = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

def cleanText(doc):
    tokens = doc.split()
    table = str.maketrans('', '', punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    tokens = [ps.stem(token) for token in tokens]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    tokens = ' '.join(tokens)
    return tokens

labels = ['Real Job', 'Fraudulent Job']

def getModel():
    extension_cnn2d = Sequential()
    extension_cnn2d.add(Convolution2D(32, (3 , 3), input_shape = (32, 24, 1), activation = 'relu'))
    extension_cnn2d.add(MaxPooling2D(pool_size = (2, 2)))
    extension_cnn2d.add(Convolution2D(32, (3, 3), activation = 'relu'))
    extension_cnn2d.add(MaxPooling2D(pool_size = (2, 2)))
    extension_cnn2d.add(Flatten())
    extension_cnn2d.add(Dense(units = 256, activation = 'relu'))
    extension_cnn2d.add(Dense(units = 2, activation = 'softmax'))
    extension_cnn2d.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    extension_cnn2d.load_weights("model/cnn2d_weights.hdf5")
    return extension_cnn2d



@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/PredictAction', methods=['GET', 'POST'])
def PredictAction():
    if request.method == 'POST':
        job_desc = request.form.get('job_desc')
        if not job_desc or job_desc.strip() == "":
            return render_template('result.html', msg="Please enter job description")
        extension_cnn2d = getModel()
        text = job_desc.strip().lower()
        text = cleanText(text)
        temp = [text]
        bert_encode = berts.encode(temp)
        bert_encode = np.reshape(bert_encode, (bert_encode.shape[0], 32, 24, 1))
        predict = extension_cnn2d.predict(bert_encode)
        pred = np.argmax(predict[0])
        output = ""
        output += "Job Details = " + job_desc[:500] + "...<br/><br/>"
        output += "Predicted Job Type ====> " + labels[pred]

        return render_template('result.html', msg=output)

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route("/signup")
def signup():
    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')

    con = sqlite3.connect('signup.db')
    cur = con.cursor()

    cur.execute("insert into info (user,email,password,mobile,name) VALUES (?,?,?,?,?)",
                (username,email,password,number,name))

    con.commit()
    con.close()

    session['user'] = username
    return redirect(url_for('home'))



@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("register.html")    

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        session['user'] = mail1
        return redirect(url_for('home'))
    else:
        return render_template("signin.html")

@app.route('/profile')
def profile():

    if 'user' not in session:
        return redirect(url_for('login'))

    username = session['user']

    con = sqlite3.connect('signup.db')
    cur = con.cursor()

    cur.execute("SELECT user,email,mobile,name FROM info WHERE user=?", (username,))
    data = cur.fetchone()

    con.close()

    if data:
        return render_template(
            'profile.html',
            username=data[0],
            email=data[1],
            mobile=data[2],
            name=data[3]
        )
    else:
        return "User data not found"

    
if __name__ == '__main__':
    app.run()