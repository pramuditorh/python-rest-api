from flask import Blueprint
from flask_restful import Api
from resources.hello import hello
from resources.categories import categories
from resources.comments import comments

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(hello, '/hello')
api.add_resource(categories, '/categories')
api.add_resource(comments, '/comments')