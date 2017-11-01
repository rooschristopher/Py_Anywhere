from flask import Flask
import flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="christopherroos",
    password="r00sterr00ster",
    hostname="christopherroos.mysql.pythonanywhere-services.com",
    databasename="christopherroos$Test",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


comments = ['THis is the first one ', 'second one', 'third one']





class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

for i in comments:
    comment = Comment(content=i)
    db.session.add(comment)
    db.session.commit()


@app.route('/')
def hello_world():
    return flask.render_template('Home_Page.html' , comments=Comment.query.all())



if __name__ == '__main__':
    app.run()
