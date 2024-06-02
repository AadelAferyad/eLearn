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

    courses = storage.get_by_name(Course, course, year)
    dictionary = {}
    if courses:
        for course_i in courses:
            dictionary[course_i.id] = {
                "name": course_i.name,
                "year": course_i.year,
                "id": course_i.id
            }
        return jsonify(dictionary), 200


@view_bp.route('course/<course_id>', strict_slashes=False, methods=['DELETE'])
@jwt_required()
def delete_course(course_id=None):
    """
    Delete a specific course from the database.

    This endpoint allows for the deletion of a course by its unique identifier.

    Parameters:
    - course_id (str): The unique identifier of the course to be deleted. This parameter is required.

    Rule:
    - course should be empty
        meaning teacher and all students in this course should be (removed)/(moved to another course). 

    Responses:
    - 200: Successful deletion of the course.
    - 401: Unauthorized, invalid or missing JWT token.
    - 404: Course not found with the provided course_id.
    """

    claims = get_jwt()
    access = claims.get('role', None)

    if (access != 'director'):
        return jsonify({'error': "You don't have access to this action"}), 401

    course = storage.get(Course, course_id)

    if course:
        if course.teacher and course.student:
            students_len = len(course.student)
            return jsonify({"error": {
                "messagae": "Can't delete this course still active",
                "teacher" : 1,
                "students": students_len
                }}), 401
        course.delete()
        return jsonify({"message": "Course deleted successfully"}), 200

    return jsonify({"error": "Course doesn't exists"}), 404
