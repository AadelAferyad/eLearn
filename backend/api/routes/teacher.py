#!/usr/bin/python3
from api.routes import view_bp
from models import storage
from models.teacher import Teacher
from models.course import Course
from models.file import File
from models.person import Person
from flask_jwt_extended import jwt_required, get_jwt
from flask import jsonify, request
from api.func import image_save, allowed_images


@view_bp.route('teachers', methods=['GET'], strict_slashes=False)
@view_bp.route('teachers/<course>', methods=['GET'], strict_slashes=False)
@view_bp.route('teachers/<course>/<year>', methods=['GET'], strict_slashes=False)
@jwt_required()
def teachers(course=None, year=None):
    """ get all teachers"""
    claims = get_jwt()
    access = claims.get('role', None)
    if access != 'director':
        return jsonify({"error":"you don't have access rights to this content"})

    dictionary = {}

    courses = storage.get_by_name(Course, course, year)

    for course_year in courses:
        for teacher in course_year.teacher:
            path = None
            if teacher.person.image_id:
                img = storage.get(File, teacher.person.image_id)
                path = img.path
            dictionary[teacher.id] = {
                "id": teacher.id,
                "First Name": teacher.person.first_name,
                "Last Name": teacher.person.last_name,
                "Phone": teacher.person.phone,
                "Email": teacher.person.email,
                "Username": teacher.person.username,
                "Birthday": teacher.person.birthday,
                "Course": course_year.name,
                "year": course_year.year,
                "image": path
            }
    return dictionary, 200


@view_bp.route('teacher/<teacher_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_teacher(teacher_id):
    """ delete teacher with id """

    claims = get_jwt()
    access = claims.get('role', None)

    if access != 'director':
        return jsonify({'error': "You don't have access to this action"}), 401

    obj_teacher = storage.get(Teacher, teacher_id)

    if obj_teacher:
        obj_person = storage.get(Person, obj_teacher.person.id)
        obj_teacher.delete()
        obj_person.delete()
 
        return jsonify({"message": "User deleted successfully"}), 200

    return jsonify({"error": "User doesn't exists"}), 404



@view_bp.route('teacher', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_teacher():
    """
        add new teacher
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
    teacher = Teacher(person_id=person.id, course_id=courses.id)
    person.save()
    teacher.save()

    return jsonify({"message": "new user has been added!"}), 200



@view_bp.route('teacher/<teacher_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_teacher(teacher_id=None):
    """
        update teacher
    """
    key_ignore = ['id', 'updated_at', 'created_at', 'year']

    if (not teacher_id):
        return jsonify({"error": "Missing teacher id"}), 400

    teacher = storage.get(Teacher, teacher_id)
    if teacher is None:
        return jsonify({"error": "teacher does't exists"}), 404

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

    person = storage.get(Person, teacher.person_id)

    for key, value in data.items():
        if key == 'course_id':
            setattr(teacher, key, value)
        if key not in key_ignore:
            setattr(person, key, value)
    person.save()
    teacher.save()
    return jsonify({}), 200
