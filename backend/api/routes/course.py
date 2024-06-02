#!/usr/bin/python3
from api.routes import view_bp
from models import storage
from models.course import Course
from flask_jwt_extended import jwt_required, get_jwt
from flask import jsonify, request


@view_bp.route('courses', strict_slashes=False, methods=['GET'])
@view_bp.route('courses/<course>', strict_slashes=False, methods=['GET'])
@view_bp.route('courses/<course>/<year>', strict_slashes=False, methods=['GET'])
@jwt_required()
def courses():
    """
    return  all courses
    """

    courses = storage.get(Course)
    dictionary = {}
    if courses:
        for course in courses:
            dictionary[course.id] = {
                "name": course.name,
                "year": course.year,
                "id": course.id
            }
        return jsonify(dictionary), 200
