#!/usr/bin/python3
from api.routes.admin import admin_bp
from models import storage
from models.student import Student
from models.course import Course
from models.person import Person
from flask_jwt_extended import jwt_required, get_jwt
from flask import jsonify, request, abort



@admin_bp.route('students/<course>', methods=['GET'], strict_slashes=False)
@admin_bp.route('students', methods=['GET'], strict_slashes=False)
@jwt_required()
def students(course=None):
    """ get all students"""
    claims = get_jwt()
    access = claims.get('role', None)
    if access != 'director' and access != 'teacher':
        return jsonify({"error":"you don't have access rights to this content"})
    dictionary = {}
    if not course:
        students = storage.get(Student)
        for student in students:
            dictionary[student.id] = {
                "id": student.id,
                "First Name": student.person.first_name,
                "Last Name": student.person.last_name,
                "Phone": student.person.phone,
                "Email": student.person.email,
                "Username": student.person.username,
                "Birthday": student.person.birthday,
                "Course": student.course.name,
                "year": student.course.year,
                "image": student.person.image.path
            }
        return dictionary, 200

    courses = storage.get_by_name(Course, course)
    for j in range(2):
        for i in courses[j].student:
            dictionary[i.id] = {
                "id": i.id,
                "First Name": i.person.first_name,
                "Last Name": i.person.last_name,
                "Phone": i.person.phone,
                "Email": i.person.email,
                "Username": i.person.username,
                "Birthday": i.person.birthday,
                "Course": courses[j].name,
                "year": courses[j].year
            }
        return dictionary, 200




@admin_bp.route('student/<student_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_student(student_id):
    """ delete student with id """
    claims = get_jwt()
    if claims.get('role', None) == 'director':
        obj_student = storage.get(Student, student_id)
        if obj_student:
            obj_person = storage.get(Person, obj_student.person.id)
            obj_student.delete()
            obj_person.delete()
            return jsonify({}), 200
    return jsonify({"error": "User doesn't exists"}), 404


@admin_bp.route('student', methods=['POST'], strict_slashes=False)
# @jwt_required()
def add_student():
    """
        add new student
    """
    # data = request.get_json()
    # if data is None:
    #     abort(400, "Not a JSON data")
    first_name = request.form.get('firstName', None)
    last_name = request.form.get('lastName', None)
    email = request.form.get('email', None)
    username = request.form.get('username', None)
    phone = request.form.get('phone', None)
    password = request.form.get('password', None)
    course = request.form.get('course', None)
    year = request.form.get('year', None)
    birthday = request.form.get('birthday', None)
    if not first_name:
        abort(400, "Messing First Name")
    if not last_name:
        abort(400, "Messing Last Name")
    if not email:
        abort(400, "Messing Email")
    if not phone:
        abort(400, "Messing Phone")
    if not username:
        abort(400, "Messing Username")
    if not password:
        abort(400, "Messing Password")
    if not course:
        abort(400, "Messing Course")

    courses = storage.get_by_name(Course, course)
    for i in courses:
        if i.year == int(year):
            courses = i
            break

    user = storage.check_username(username)
    if user:
        abort(400, "This username aleardy taken")
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'username': username,
        'password': password,
        'birthday': birthday
        }

    person = Person(**data)
    student = Student(person_id=person.id, course_id=courses.id)
    person.save()
    student.save()

    #image not implenated yet
    return jsonify({"message": "new user has been added!"}), 200


@admin_bp.route('student/<student_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_student(student_id):
    """
        update student
    """
    key_ignore = ['id', 'updated_at', 'created_at', 'year']

    student = storage.get(Student, student_id)
    if student is None:
        abort(404)
    person = storage.get(Person, student.person.id)
    data = dict(request.form)
    if not data:
        abort(400, "Not a JSON")

    for key, value in data.items():
        if key == 'course':
            year = data.get
            setattr(student, key, value)
        if key not in key_ignore:
            setattr(person, key, value)
    person.save()
    student.save()
    return jsonify({}), 200
