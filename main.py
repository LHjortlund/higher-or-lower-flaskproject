from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    return ('<h1 style="text-align: center">Learning Flask</h1>'
            '<p>Learn More Be Smart</p>'
            '<img src="https://d2zp5xs5cp8zlg.cloudfront.net/image-61785-800.jpg">')


if __name__ == '__main__':
    app.run(debug=True)