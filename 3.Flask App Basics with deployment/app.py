from flask import Flask, abort, request

app = Flask(__name__)

@app.route("/")
def two_hundred():
    return "<h1>200! All is good from duke university</h1>"

@app.route("/error")
def error():
    return abort(500, "OOOhh, some error!")

@app.route("/predict", methods = ["POST"])
def predict():
    # Predict logic goes here
    # request.json[0] can be used to fetch the string sentence sent
    # in the body of the request
    return request.json[0]


if __name__ == "__main__":
    app.run(debug = True, port = 8000, host = "0.0.0.0")