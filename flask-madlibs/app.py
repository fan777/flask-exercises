from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "secretzkeyz123"
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    # print(story.prompts, flush=True)
    '''Shows home page'''
    return render_template('home.html', prompts=story.prompts)


@app.route('/story')
def story_page():
    # answers = {prompt:request.args[prompt] for prompt in story.prompts }
    # this_story = story.generate(answers)
    text = story.generate(request.args)
    return render_template('story.html', text=text)
