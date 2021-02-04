from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "secretzkeyz123"
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_page():
  '''Shows home page'''
  return render_template('home.html', survey=satisfaction_survey)

@app.route('/start', methods=["POST"])
def start_page():
  '''start question'''
  responses = []
  return redirect(f'/question/{len(responses)}')

@app.route('/question/<int:id>')
def question_page(id):
  # if done
  if (len(responses) == len(satisfaction_survey.questions)):
    return redirect('/done')
  # if out of order
  if (len(responses) != id):
    return redirect(f'/question/{len(responses)}')
  return render_template('question.html', question=satisfaction_survey.questions[id])

@app.route('/answer', methods=["POST"])
def save_answer():
  # get choice
  choice = request.form['answer']
  # save choice
  responses.append(choice)
  # if done
  if (len(responses) == len(satisfaction_survey.questions)):
    return redirect('/done')
  # if next question
  else:
    return redirect(f'/question/{len(responses)}')

@app.route('/done')
def thank_you():
  return render_template('done.html', responses=responses)