from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'


@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"


@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}<h1>".format(name)


@app.route('/error/<name>')
def error(name):
    return "100th letter {}".format(name[100])


@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] == 'y':
        name = name[:-1] + 'iful'
    else:
        name = name + 'y'

    return '<h1>{}</h1>'.format(str.capitalize(name))


if __name__ == '__main__':
    app.run(debug=True)
