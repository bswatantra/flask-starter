from flask import Flask
from app.blueprints import web, users
from app.extentions import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

app.register_blueprint(web.bp)
app.register_blueprint(users.bp)

with app.app_context():
    db.create_all()
