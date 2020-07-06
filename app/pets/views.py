from flask import Blueprint, render_template, request
from app.forms import PetForm

pets = Blueprint('pets', __name__, template_folder='templates', static_folder='static')


@pets.route('/')
def main_p():
    return render_template('pets/index_p.html')