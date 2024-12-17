from flask import Blueprint, render_template, request, flash, redirect, url_for

import bcrypt
from .models import *
from . import db
from flask_login import login_user, login_required, logout_user, current_user

import re

auth = Blueprint("auth", __name__)

# Regular expression for email validation
regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
# re.fullmatch(regex, email)
