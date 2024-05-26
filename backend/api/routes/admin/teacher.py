#!/usr/bin/python3
from api.routes.admin import admin_bp
from models import storage
from models.teacher import Teacher
from models.person import Person
from flask_jwt_extended import jwt_required, get_jwt
from flask import jsonify, request, abort

@admin_bp.route('teachers', methods=['GET'], strict_slashes=False)
@jwt_required()
def teachers():
    """ get all teachers"""
    claims = get_jwt()
    if claims.get('role', None) == 'director':
        dictionary = {}
        teachers = storage.get(Teacher)
        for teacher in teachers:
            dictionary[teacher.id] = {
                "id": teacher.id,
                "First Name": teacher.person.first_name,
                "Last Name": teacher.person.last_name,
                "Phone": teacher.person.phone,
                "Course": teacher.course.name,
                "Email": teacher.person.email,
                "Username": teacher.person.username,
                "Birthday": teacher.person.birthday
            }
        return dictionary, 200


@admin_bp.route('teacher/<teacher_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_teacher(teacher_id):
    """ delete teacher with id """
    claims = get_jwt()
    if claims.get('role', None) == 'director':
        obj_teacher = storage.get(Teacher, teacher_id)
        if obj_teacher:
            obj_person = storage.get(Person, obj_teacher.person.id)
            obj_teacher.delete()
            obj_person.delete()
            return jsonify({}), 200
    return jsonify({"error": "User doesn't exists"}), 404



@admin_bp.route('teacher', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_teacher():
    """
        add new student
    """
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON data")
    if 'first_name' not in data:
        abort(400, "Messing First Name")
    if 'last_name' not in data:
        abort(400, "Messing Last Name")
    if 'email' not in data:
        abort(400, "Messing Email")
    if 'phone' not in data:
        abort(400, "Messing Phone")
    if 'username' not in data:
        abort(400, "Messing Username")
    if 'password' not in data:
        abort(400, "Messing Password")
    if 'course_id' not in data:
        abort(400, "Messing Course")

    user = storage.check_username(data.get('username', None))
    if user:
        abort(400, "This username aleardy taken")
    course_id = data.get('course_id')
    del data['course_id']
    person = Person(**data)
    teacher = Teacher(person_id=person.id, course_id=course_id)
    person.save()
    teacher.save()

    #image not implenated yet
    return jsonify({}), 200


@admin_bp.route('teacher/<teacher_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_teacher(student_id):
    """
        update student
    """
    key_ignore = ['id', 'updated_at', 'created_at']

    teacher = storage.get(Teacher, teacher_id)
    if student is None:
        abort(404)
    person = storage.get(Person, teacher.person.id)
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")

    for key, value in data.items():
        if key == 'course_id':
            setattr(teacher, key, value)
        if key not in key_ignore:
            setattr(person, key, value)
    person.save()
    teacher.save()
    return jsonify({}), 200