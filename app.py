from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/users")
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users])

if __name__ == "__main__":
    app.run(debug=True)
