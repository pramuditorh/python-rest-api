from flask_restful import Resource


class hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}