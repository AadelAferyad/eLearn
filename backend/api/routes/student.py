#!/usr/bin/python3
from api.routes import view_bp
from models import storage
from models.student import Student
from models.course import Course
from models.teacher import Teacher
from models.file import File
from models.person import Person
from flask_jwt_extended import jwt_required, get_jwt, current_user
from flask import jsonify, request
from api.func import image_save, allowed_images


@view_bp.route('students', methods=['GET'], strict_slashes=False)
@view_bp.route('students/<course>', methods=['GET'], strict_slashes=False)
@view_bp.route('students/<course>/<year>', methods=['GET'], strict_slashes=False)

@jwt_required()
def students(course=None, year=None):
    """ get all students"""
    claims = get_jwt()
    access = claims.get('role', None)
    if access != 'director' and access != 'teacher':
        return jsonify({"error":"you don't have access rights to this content"})

    if access == 'teacher':
        user = storage.role(Teacher, current_user.id)
        course = user.course.name
        year = user.course.year

    dictionary = {}

    courses = storage.get_by_name(Course, course, year)

    for course_year in courses:
        for student in course_year.student:
            path = None
            if student.person.image_id:
                img = storage.get(File, student.person.image_id)
                path = img.path
            dictionary[student.id] = {
                "id": student.id,
                "First Name": student.person.first_name,
                "Last Name": student.person.last_name,
                "Phone": student.person.phone,
                "Email": student.person.email,
                "Username": student.person.username,
                "Birthday": student.person.birthday,
                "Course": course_year.name,
                "year": course_year.year,
                "image": path
            }
    return dictionary, 200


@view_bp.route('student/<student_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_student(student_id):
    """ delete student with id """

    claims = get_jwt()
    access = claims.get('role', None)

    if access != 'director':
        return jsonify({'error': "You don't have access to this action"}), 401

    obj_student = storage.get(Student, student_id)

    if obj_student:
 
        obj_person = storage.get(Person, obj_student.person.id)
        obj_student.delete()
        obj_person.delete()
 
        return jsonify({"message": "User deleted successfully"}), 200

    return jsonify({"error": "User doesn't exists"}), 404


@view_bp.route('student', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_student():
    """
        add new student
    """

    claims = get_jwt()
    access = claims.get('role', None)

    if access != 'director':
        return jsonify({'error': "You don't have access to this action"}), 401

    first_name = request.form.get('firstName', None)
    last_name = request.form.get('lastName', None)
    email = request.form.get('email', None)
    username = request.form.get('username', None)
    phone = request.form.get('phone', None)
    password = request.form.get('password', None)
    course = request.form.get('course', None)
    year = request.form.get('year', None)
    birthday = request.form.get('birthday', None)
    image = request.files.get('image', None)

    if not first_name:
        return jsonify({"error": "Messing First Name"}), 400
    if not last_name:
        return jsonify({"error": "Messing Last Name"}), 400
    if not email:
        return jsonify({"error": "Messing Email"}), 400
    if not phone:
        return jsonify({"error": "Messing Phone"}), 400
    if not username:
        return jsonify({"error": "Messing Username"}), 400
    if not password:
        return jsonify({"error": "Messing Password"}), 400
    if not course:
        return jsonify({"error": "Messing Course"}), 400

    data = {}
    path = None
    courses = storage.get_by_name(Course, course, year)[0]

    user = storage.check_username(username)

    if user:
        return jsonify({"error": "This username aleardy taken"}), 400

    if image:
        file = File(name=image.filename, path='nill')
        image_list = image.filename.split('.')
        image_extention = image_list[-1].lower()
        if not allowed_images(image_extention):
            return jsonify({"error": "Unallowed file type"}), 400
        image_name = file.id + '.' + image_extention
        file.path = image_name
        file.save()
        image_save(image, image_name)
        path = file.id

    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'username': username,
        'password': password,
        'birthday': birthday,
        'image_id': path
        }

    person = Person(**data)
    student = Student(person_id=person.id, course_id=courses.id)
    person.save()
    student.save()

    return jsonify({"message": "new user has been added!"}), 200


@view_bp.route('student/<student_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_student(student_id=None):
    """
        update student
    """
    key_ignore = ['id', 'updated_at', 'created_at', 'year']

    if (not student_id):
        return jsonify({"error": "Missing student id"}), 400

    student = storage.get(Student, student_id)
    if student is None:
        return jsonify({"error": "student does't exists"}), 404

    data = {}

    first_name = request.form.get('firstName', None)
    last_name = request.form.get('lastName', None)
    email = request.form.get('email', None)
    username = request.form.get('username', None)
    phone = request.form.get('phone', None)
    password = request.form.get('password', None)
    course = request.form.get('course', None)
    year = request.form.get('year', None)
    birthday = request.form.get('birthday', None)
    image = request.files.get('image', None)

    if first_name:
        data['first_name'] = first_name        
    if last_name:
        data['last_name'] = last_name
    if email:
        data['email'] = email
    if phone:
        data['phone'] = phone
    if username:
        data['username'] = username
    if password:
        data['password'] = password
    if course:
        courses = storage.get_by_name(Course, course, year)
        data['course_id'] = courses[0].id
    if birthday:
        data['birthday'] = birthday
    if image:
        file = File(name=image.filename, path='nill')
        image_list = image.filename.split('.')
        image_extention = image_list[-1].lower()
        if not allowed_images(image_extention):
            return jsonify({"error": "Unallowed file type"}), 400
        image_name = file.id + '.' + image_extention
        file.path = image_name
        file.save()
        image_save(image, image_name)
        data['image_id'] = file.id

    person = storage.get(Person, student.person_id)

    for key, value in data.items():
        if key == 'course_id':
            setattr(student, key, value)
        if key not in key_ignore:
            setattr(person, key, value)
    person.save()
    student.save()
    return jsonify({}), 200
