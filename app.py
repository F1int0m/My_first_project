import os

from flask import Flask, render_template
import dotenv

app = Flask(__name__)
dotenv.load_dotenv()


@app.route('/')
def index():
    return render_template('123.html', secret=os.getenv('secret'))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
