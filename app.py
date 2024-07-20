from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Lencinas Oscanoa Eric Brayan</h2>'


if __name__ == "__main__":
    app.run(debug=True)
