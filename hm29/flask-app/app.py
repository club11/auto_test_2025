"""Application Cat view """

import random
from flask import Flask, render_template

app = Flask(__name__)

# list of cat images
images = [
    "https://media.tenor.com/t0eFbcxLGgIAAAAC/fat-cat-laser-eyes.gif",
    "https://media.tenor.com/pOS38tUuVnQAAAAd/cat-meme.gif",
    "https://media.tenor.com/lQlIBQeeruwAAAAd/wanted-cat.gif"
    ]


@app.route('/')
def index():
    """render template"""
    url = random.choice(images)
    return render_template('index.html', url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8866")
