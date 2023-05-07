from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from rake_nltk import Rake
from textblob import TextBlob
import re

r = Rake()


#from summarizer import Summarizer

#model = Summarizer()

@app.route("/generateQuestions", methods=["POST"])
@cross_origin()
def generateQuestions():
    input = eval(request.data.decode('UTF-8'))["input"]
    #result = model(input, min_length=6, max_length = 100, ratio = 0.4)
    #summarized_text = ''.join(result)
    #print (input)
    #r.extract_keywords_from_text(input)
    #scored = r.get_ranked_phrases()
    sentences = re.split('[^0-9]["."][^0-9]', input)
    questions = []
    answers = []
    for sent in sentences: 
        blob = TextBlob(sent)
        answer = blob.noun_phrases[0]
        answers.append(answer)
        questions.append(sent.lower().replace(answer, "___"))
        #r.extract_keywords_from_text(sent)
        #questions.append(sent.lower().replace(r.get_ranked_phrases()[0], "___"))
    #print(questions)
    return [questions, answers]
    #return [input]

if __name__ == "__main__":
    app.run(debug=True)