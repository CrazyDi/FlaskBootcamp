import os
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = 'true'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

blueprint = make_google_blueprint(client_id='9400940270-ad3u5f9tpte5tbb6kuvrapjau5c3sf22.apps.googleusercontent.com', client_secret='c8w8Dh4nIJKbHqalbFqGyXvy', offline=True, scope=['profile', 'email'])
app.register_blueprint(blueprint, url_prefix='/login')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/welcome')
def welcome():
    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html', email=email)


@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))

    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html', email=email)


if __name__ == "__main__":
    app.run(debug=True)
