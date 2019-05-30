import os

import flask

import blueprints.docker
import blueprints.jenkins
import blueprints.gitlab

app = flask.Flask(__name__)

app.register_blueprint(blueprints.docker.blueprint)
app.register_blueprint(blueprints.jenkins.blueprint)
app.register_blueprint(blueprints.gitlab.blueprint)

@app.route('/', methods=[ 'GET' ])
def index():
    return flask.redirect('/docker')

if __name__ == '__main__':

    os.environ['FLASK_APP'] = 'app.py'
    os.environ['FLASK_ENV'] = 'development'

    app.run()