from flask import Flask, request, render_template, redirect, flash
from flask import session, make_response
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "secretzkeyz123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#responses = []

@app.route('/')
def home_page():
  '''Shows home page'''
  return render_template('home.html', survey=satisfaction_survey)

@app.route('/start', methods=["POST"])
def start_page():
  '''start question'''
  #responses = []
  responses = []
  session['responses'] = responses
  return redirect(f'/question/{len(responses)}')

@app.route('/question/<int:id>')
def question_page(id):
  responses = session.get('responses')
  # if done
  if (len(responses) == len(satisfaction_survey.questions)):
    flash(f'Survey already complete!')
    return redirect('/done')
  # if out of order
  if (len(responses) != id):
    flash(f'Error:  Attempting to access question {qid} out of order!  Returning to question.')
    return redirect(f'/question/{len(responses)}')
  return render_template('question.html', question=satisfaction_survey.questions[id])

@app.route('/answer', methods=["POST"])
def save_answer():
  # get choice
  choice = request.form['answer']
  # save choice
  responses = session['responses']
  responses.append(choice)
  session['responses'] = responses
  # if done
  if (len(responses) == len(satisfaction_survey.questions)):
    return redirect('/done')
  # if next question
  else:
    return redirect(f'/question/{len(responses)}')

@app.route('/done')
def thank_you():
  responses = session.get('responses')
  return render_template('done.html', responses=responses)