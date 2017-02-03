from flask import Flask, request, abort, flash, redirect, url_for
from database import appmodel as db
from config import config
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from logmanager import log

app = Flask(__name__)
app.config.from_object(config)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/home"

@login_manager.user_loader
def load_user(id):
    #if id is None or id == 'None': id = -1 #None breaks peewee ugly... :(
    try:
        user = db.Users.get(db.Users.id == id)
        return user
    except: return None

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/register", methods=['POST'])
def register():
    if set((request.form.keys())) != set(['username', 'password', 'email']): return abort(400)
    try:
        user = db.Users(username = request.form['username'],
                        password = generate_password_hash(request.form['password']),
                        email    = request.form['email'],)
        user.save()
    except: abort(400)
    return "ok" # this easily can by json or redirect, but now is rammus

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try: user = db.Users.select().where(db.Users.username == username).get()
    except:
        log.warning('username does not exist')
        logout_user()
        abort(401)
    login_user(user)
    if check_password_hash(user.password, password):
        flash('Logged in successfully'+str(user.id))

        #if not is_safe_url(next): return flask.abort(400) FIXIT: security issue
        return "ok" #redirect(next or url_for('index'))

    log.warning('invalid password')
    logout_user()
    abort(401)


if __name__ == "__main__":
    app.run()
