from flask import Flask
import flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="<christopherroos>",
    password="<r00ster>",
    hostname="<christopherroos.mysql.pythonanywhere-services.com>",
    databasename="<christopherroos$Test>",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))




@app.route('/')
def hello_world():
    return flask.render_template('Home_Page.html')



if __name__ == '__main__':
    app.run()
