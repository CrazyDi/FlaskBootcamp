from flask import Flask, render_template, request
import re


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    username = request.args.get('name')

    error_list = []

    if re.search('[A-Z]', username) is None:
        error_list.append('You did not use an uppercase character.')

    if re.search('[a-z]', username) is None:
        error_list.append('You did not user a lowercase character.')

    if re.search('\d+$', username) is None:
        error_list.append('You did not end your username with a number.')

    error = len(error_list) > 0

    return render_template('report.html', error=error, error_list=error_list)


if __name__ == "__main__":
    app.run(debug=True)
