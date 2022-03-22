from flask import Flask, render_template, request, url_for, redirect
from markupsafe import escape
from models import Document, Authors
from db import DOCUMENTS,AUTHORS
from Forms import regist_doc

app = Flask(__name__)
app.config['SECRET_KEY'] = '8f8866aec15fb97de69229e4'

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/documents", methods=['GET', 'POST'])
def add_documents():
    form = regist_doc()
    if form.validate_on_submit():
        doc = Document(
            form.doc_id.data,
            form.doc_tit.data,
            form.doc_numop.data,
            form.doc_cat.data,
            form.doc_auth.data
            )

        DOCUMENTS.append(doc.__str__.__dict__())
        return redirect(url_for('home'))

    return render_template('documents.html', DOCUMENTS = DOCUMENTS, form=form)

@app.route('/authors')
@app.route('/authors/<name>')
def authors_profile(name = None):
    # show the user profile for that user
    return render_template('authors.html', name = name)


@app.route('/about')
def about():
    return 'The about page'


    