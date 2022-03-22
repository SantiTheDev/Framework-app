from cProfile import label
from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class regist_doc(FlaskForm):
    doc_id = StringField(label='ID')
    doc_tit = StringField(label='title')
    doc_numop = StringField(label='number of pages')
    doc_cat = StringField(label='category')
    doc_auth = StringField(label='author')
    submit = SubmitField(label='Create doc')