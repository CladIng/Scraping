from flask import Flask
app = Flask(__name__)

@app.route("/api/<name>")
def hello(name):
    return "Hello cesar %s" % name

if __name__ == "__main__":
    app.run()