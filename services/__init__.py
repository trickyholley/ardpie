from flask import Blueprint
from users import UserService

# Create a blueprint
user_blueprint = Blueprint('user', __name__)

# Register the routes for UserService with the blueprint
user_blueprint.add_url_rule('/users', 'get_all_users', UserService.get_all_users, methods=['GET'])
user_blueprint.add_url_rule('/users/<int:user_id>', 'get_user', UserService.get_user, methods=['GET'])
user_blueprint.add_url_rule('/users', 'create_user', UserService.create_user, methods=['POST'])
user_blueprint.add_url_rule('/users/<int:user_id>', 'update_user', UserService.update_user, methods=['PUT'])
user_blueprint.add_url_rule('/users/<int:user_id>', 'delete_user', UserService.delete_user, methods=['DELETE'])
user_blueprint.add_url_rule('/login', 'login', UserService.login, methods=['POST'])

# Expose user_blueprint for use in other files
__all__ = ['user_blueprint']
