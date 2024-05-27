import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 
    'postgresql://psqladmin%40daniapppsqlserver:AdminPassword123%21@daniapppsqlserver.postgres.database.azure.com:5432/exampledb?sslmode=disable'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50), unique=True, nullable=False)

@app.route('/')
def home():
    unique_visitors = Visitor.query.count()
    return f'Unique Visitors: {unique_visitors}'

@app.route('/version')
def version():
    return jsonify({"version": "1.0.0"})

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/visit', methods=['POST'])
def visit():
    ip_address = request.remote_addr
    if not Visitor.query.filter_by(ip_address=ip_address).first():
        new_visitor = Visitor(ip_address=ip_address)
        db.session.add(new_visitor)
        db.session.commit()
    return 'Visit recorded', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
