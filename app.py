from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLAlchemy part
# Replace 'mysql+pymysql://username:password@localhost/mydatabase' with your actual MySQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://python-user:@/python_test?unix_socket=/cloudsql/hale-mercury-415809:us-central1:mysql-db/mysql-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Initialize the database
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return jsonify({'message':'hello world'})

# Route to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201

# Route to get a user by username
@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'username': user.username, 'email': user.email}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
    
