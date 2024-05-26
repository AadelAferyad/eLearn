#!/usr/bin/python3
from flask import Blueprint
admin_bp = Blueprint('admin', __name__)
from api.routes.admin.teacher import *
from api.routes.admin.student import *
from api.routes.admin.course import *