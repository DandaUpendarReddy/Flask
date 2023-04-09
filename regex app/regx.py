from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/matches', methods=['POST'])
def matches():
    test_string = request.form['test_string']
    regex_input = request.form.get('regex_input')
    matches = re.findall(regex_input, test_string)
    return render_template('matches.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
