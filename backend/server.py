from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/generateQuestions", methods=["POST"])
@cross_origin()
def generateQuestions():
    input = eval(request.data.decode('UTF-8'))["input"]
    return [input]

if __name__ == "__main__":
    app.run(debug=True)