from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_container():
    return "Hello container"

@app.route("/html")
def hello_container_html():
    return "<h1>Hello container</h1>"

if __name__ == '__main__':
   app.run('0.0.0.0','8080')