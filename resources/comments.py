from flask import request
from http import HTTPStatus
from flask_restful import Resource
from Model import db, Comment, CommentSchema

comments_schema = CommentSchema(many=True)

class comments(Resource):
    def get(self):
        comments = Comment.query.all()
        comments = comments_schema.dump(comments).data

        return {"status" : "success", "data" : comments, "message" : "get comments", "http_status" : HTTPStatus.OK}