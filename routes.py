from flask import Blueprint, jsonify
from .models import db, User  # Import db and User model from models.py

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users])

@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

@user_routes.route('/users', methods=['POST'])
def create_user():
    # Example for creating a new user
    new_user = User(name="New User", email="newuser@example.com")
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully", "id": new_user.id}), 201

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    # Example for updating user information
    user.name = "Updated Name"
    user.email = "updated@example.com"
    db.session.commit()
    return jsonify({"message": "User updated successfully", "id": user.id})

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully", "id": user.id})
