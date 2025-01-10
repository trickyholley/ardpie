import jwt
import datetime
from werkzeug.security import check_password_hash
from sqlalchemy import text, create_engine
from flask import request, jsonify

# Setup a connection to the database
DATABASE_URL = "sqlite:///your_database.db"  # Use your actual DB connection
engine = create_engine(DATABASE_URL)


class UserService:
    @staticmethod
    def get_all_users():
        # Logic to fetch all users (example implementation)
        return jsonify({"message": "Get all users"}), 200

    @staticmethod
    def get_user(user_id):
        # Logic to get a user by ID
        return jsonify({"message": f"Get user with id {user_id}"}), 200

    @staticmethod
    def create_user():
        # Logic to create a user
        data = request.get_json()
        return jsonify({"message": "User created", "data": data}), 201

    @staticmethod
    def update_user(user_id):
        # Logic to update a user's details
        data = request.get_json()
        return jsonify({"message": f"User with id {user_id} updated", "data": data}), 200

    @staticmethod
    def delete_user(user_id):
        # Logic to delete a user by ID
        return jsonify({"message": f"User with id {user_id} deleted"}), 200

    @staticmethod
    def login():
        # Login logic with JWT
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        try:
            query = text("SELECT id, name, password FROM users WHERE name = :name")
            with engine.connect() as connection:
                result = connection.execute(query, {"name": username}).fetchone()

            if result:
                user_id, fetched_name, hashed_password = result
                if check_password_hash(hashed_password, password):
                    payload = {
                        "user_id": user_id,
                        "username": fetched_name,
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                    }
                    token = jwt.encode(payload, "your_secret_key", algorithm="HS256")
                    return jsonify({"message": "Login successful", "token": token}), 200

                return jsonify({"error": "Invalid password"}), 401
            else:
                return jsonify({"error": "User not found"}), 404
        except Exception as e:
            print(f"Error during login: {e}")
            return jsonify({"error": "An error occurred while logging in"}), 500
