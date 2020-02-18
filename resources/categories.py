from flask import request
from http import HTTPStatus
from flask_restful import Resource
from Model import Category, CategorySchema

categories_schema = CategorySchema(many=True)

class categories(Resource):
    def get(self):
        categories = Category.query.all()
        categories = categories_schema.dump(categories).data
        return {"status" : "success", "data" : categories, "message" : "get categories", "http_status" : HTTPStatus.OK}

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(name=data['name']).first()
        if category:
            return {'message': 'Category already exists'}, 400
        category = Category(
            name=json_data['name']
            )

        db.session.add(category)
        db.session.commit()

        result = category_schema.dump(category).data

        return { "status": 'success', 'data': result }, 201