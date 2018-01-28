import json
from flask import jsonify
from flask import Flask, render_template, request
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('input.html')

@app.route('/result', methods=['POST'])
def result():
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        username='*****************',
        password='*************',
        version='2017-02-27')

    if request.method == 'POST':
        text1 = request.form
        user = natural_language_understanding.analyze(
        text=str(text1),
        features=Features(
            entities=EntitiesOptions(
                emotion=True,
                sentiment=True,
                limit=2),
            keywords=KeywordsOptions(
                emotion=True,
                sentiment=True,
                limit=2)))
        return jsonify(user)
        #return render_template("result.html", result=user)

if __name__ == '__main__':
 app.run(debug=True)
