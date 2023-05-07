from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from summarizer import Summarizer

model = Summarizer()

@app.route("/generateQuestions", methods=["POST"])
@cross_origin()
def generateQuestions():
    input = eval(request.data.decode('UTF-8'))["input"]
    result = model(input, min_length=6, max_length = 100, ratio = 0.4)
    summarized_text = ''.join(result)
    print (summarized_text)
    return [summarized_text]

if __name__ == "__main__":
    app.run(debug=True)