from turtle import title
from unicodedata import category
from urllib.request import Request
from flask import Flask, render_template, request, url_for, redirect
from markupsafe import escape
from models import Document, Authors
from db import DOCUMENTS,AUTHORS

app = Flask(__name__)
app.config['SECRET_KEY'] = '8f8866aec15fb97de69229e4'

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/documents", methods=['GET', 'POST'])
def documents():
    Request = request
    return render_template('documents.html', DOCUMENTS = DOCUMENTS, request=Request)

@app.route('/add_document', methods = ['GET'])
def add_document():
    return render_template('docform.html')


@app.route('/authors', methods=['GET', 'POST'])
def authors(name = None):
    # show the user profile for that user
    return render_template('authors.html', AUTHORS = AUTHORS )

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    return render_template('autform.html')

@app.route('/form', methods=["POST"])
def form():
    if request.form.get("name"):
        name = request.form.get("name")
        author = Authors(name)
        AUTHORS.append(author.__dict__)
    else:
        id = request.form.get("id")
        title = request.form.get("title")
        numberOfPages= request.form.get("number_of_pages")
        authors= request.form.get("authors")
        category= request.form.get("category")

        doc = Document(id,title,numberOfPages,category,authors)
        DOCUMENTS.append(doc.__dict__)

    
    return render_template('submitform.html')


@app.route('/about')
def about():
    return render_template('index.html')


    