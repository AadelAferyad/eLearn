#!/usr/bin/python3
from flask import Blueprint
auth_bp = Blueprint('auth', __name__)
view_bp = Blueprint('view', __name__)
from api.routes.auth import *
from api.routes.teacher import *
from api.routes.student import *
from api.routes.course import *