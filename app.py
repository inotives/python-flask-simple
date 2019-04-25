# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, BooleanField

app = Flask(__name__)
app.config.from_object('config')


class SampleForm(Form):
    name = TextField("Name:", validators=[validators.required() ])
    ismarried = BooleanField("Married")

# Routing the path
@app.route('/', methods=['GET', 'POST'])
def index():
    link_to_form = {'url': '/form'}
    return render_template('home.html', link=link_to_form)


@app.route('/form', methods=['GET', 'POST'])
def test_form():
    print(request.form)
    form = SampleForm(request.form)
    return render_template('form.html', form=form)


@app.route('/process_form', methods=["POST"])
def process_form():
    if request.method == 'POST':
        name = request.form["name"]
        
        print("Submitted Form Object:", request.form)
        
    # Return page after processing
    return render_template("form_submitted.html", name=name)


if __name__ == "__main__":
    app.run()

