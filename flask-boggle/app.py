from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "asdfhl45lhasdf"


@app.route('/')
def homepage():
    board = boggle_game.make_board()
    session['board'] = board

    return render_template('index.html', board=board)
