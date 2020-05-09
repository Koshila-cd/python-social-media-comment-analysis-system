import main
import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/data', methods=['POST'])
def find_data():
    comment1 = request.json['comment']
    description = request.json['description']
    title = request.json['title']
    return main.toService(comment1, description, title)


app.run()
