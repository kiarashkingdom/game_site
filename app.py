from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rock-paper-scissors')
def rock_paper_scissors():
    return render_template('rock_paper_scissors.html')

@app.route('/guess-number')
def guess_number():
    return render_template('guess_number.html')

@app.route('/dice')
def dice():
    return render_template('dice.html')

@app.route('/memory')
def memory():
    return render_template('memory.html')
