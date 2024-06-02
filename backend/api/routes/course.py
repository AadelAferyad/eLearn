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
def courses(course=None, year=None):
     """
        Retrieve available courses from the database.

        This endpoint allows for fetching courses in various ways:
        - If no parameters are provided, it returns all available courses.
        - If a course name is provided, it returns information about that specific course.
        - If both a course name and a year are provided, it returns information about the specific course for that particular year.
    """

    courses = get_by_name(Course, course, year)
    dictionary = {}
    if courses:
        for course_i in courses:
            dictionary[course_i.id] = {
                "name": course_i.name,
                "year": course_i.year,
                "id": course_i.id
            }
        return jsonify(dictionary), 200
