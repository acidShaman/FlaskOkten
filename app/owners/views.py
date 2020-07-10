from flask import Blueprint, render_template, request, url_for, redirect
from app.forms import OwnerForm, PetForm
from app.owners.models import OwnerModel, PetModel
from app.owners_and_pets import owners_list
from app import db
owners = Blueprint('owners', __name__, template_folder='templates', static_folder='static')


@owners.route('/')
def show_owners():
    owners = OwnerModel.query.all()
    if not owners:
        return redirect(url_for('owners.add_owner'))
    return render_template('owners/show_all_owners.html', owners=owners)


@owners.route('/add_owner', methods=['POST', 'GET'])
def add_owner():
    form = OwnerForm(request.form)
    if request.method == 'POST' and form.validate():
        owner = OwnerModel(name=request.form['name'], age=request.form['age'], location=request.form['location'])
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for('owners.show_owners'))
    return render_template('owners/add_owner.html', form=form)


@owners.route('/<int:index>/pets/add_pet', methods=['GET', 'POST'])
def add_pet(index):
    form = PetForm(request.form)
    if request.method == 'POST' and form.validate():
        pet = PetModel(name=request.form['name'], age=request.form['age'], type_pet=request.form['type_pet'], owner_id=index)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('owners.show_pets_by_owner', index=index))
    return render_template('owners/add_pet.html', form=form)


@owners.route('/<int:index>/pets')
def show_pets_by_owner(index):
    pets_of_owner = PetModel.query.filter_by(owner_id=index)
    owner = OwnerModel.query.filter_by(id=index)
    if not pets_of_owner:
        return redirect(url_for('owners.add_pet', index=index))
    return render_template('owners/pets_of_owner.html', owner=owner, pets=pets_of_owner, index=index)


@owners.route('/all_pets')
def show_all_pets():
    all_pets = PetModel.query.all()
    return render_template('owners/all_pets.html', pets=all_pets)


@owners.route('/type=<type_pet>')
def show_owners_by_pet_type(type_pet):
    pets_of_this_type = PetModel.query.filter_by(type_pet=type_pet)
    owners_with_pet_type = []
    for pet in pets_of_this_type:
        owners_with_pet_type.append(OwnerModel.query.filter_by(id=pet.owner_id))
    return render_template('owners/show_owners_by_pet_type.html', owners=owners_with_pet_type, type_pet=type_pet)
#
#
#
#
# @owners.route('/<owner_name>/deleted')
# def delete_owner(owner_name):
#     for owner in owners_list:
#         if owner['name'] == owner_name:
#             owners_list.remove(owner)
#     return redirect(url_for('owners.show_owners'))
#
#
#
#
# @owners.route('/<int:index>/pets/<int:pet_index>/deleted')
# def delete_pet_by_id(index, pet_index):
#     for owner in owners_list:
#         if owners_list.index(owner) == index:
#             for pet in owner['pets']:
#                 if owner['pets'].index(pet) == pet_index:
#                     del owner['pets'][pet_index]
#     return redirect(url_for('owners.show_pets_by_owner', index=index))

















