from flask import Flask, render_template,request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET KEY'] = 'Secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def question():
    prompts = story.prompts

    return render_template("questions.html", promtps = prompts)

@app.route('/story')
def theStory():
    text = story.generate(request.args)

    return render_template("story.html", text = text)