from flask import Blueprint, render_template, request, url_for, redirect
from app.forms import OwnerForm, PetForm
from app.owners.models import Owner
from app.owners_and_pets import owners_list
from app import db

owners = Blueprint('owners', __name__, template_folder='templates', static_folder='static')

from .models import Owner, Pet


@owners.route('/')
def show_owners():
    if not owners_list:
        return redirect(url_for('owners.add_owner'))
    return render_template('owners/show_all_owners.html', owners=owners_list)


@owners.route('/<int:index>/pets')
def show_pets_by_owner(index):
    for owner in owners_list:
        if owners_list.index(owner) == index:
            if not owner['pets']:
                return redirect(url_for('owners.add_pet', index=index))
            return render_template('owners/pets_of_owner.html', owner_with_pets=owner, index=index)


@owners.route('/type=<pet_type>')
def show_owners_by_pet_type(pet_type):
    owners_with_pet_type = []
    for owner in owners_list:
        for pet in owner['pets']:
            if pet['type_pet'] == pet_type:
                if owner not in owners_with_pet_type:
                    owners_with_pet_type.append(owner)
    return render_template('owners/show_all_owners.html', owners=owners_with_pet_type, pet_type=pet_type)


@owners.route('/add_owner', methods=['POST', 'GET'])
def add_owner():
    db.create_all()
    form = OwnerForm(request.form)
    if request.method == 'POST' and form.validate():
        owner_data = dict(request.form)
        del owner_data['save']
        owners_list.append(Owner(**owner_data))
        return redirect(url_for('owners.show_owners'))
    return render_template('owners/add_owner.html', form=form)


@owners.route('/<owner_name>/deleted')
def delete_owner(owner_name):
    for owner in owners_list:
        if owner['name'] == owner_name:
            owners_list.remove(owner)
    return redirect(url_for('owners.show_owners'))


@owners.route('/<int:index>/pets/add_pet', methods=['GET', 'POST'])
def add_pet(index):
    form = PetForm(request.form)
    if request.method == 'POST' and form.validate():
        pet_data = dict(request.form)
        del pet_data['save']
        owners_list[index].add_pet(**pet_data)
        return redirect(url_for('owners/show_pets_by_owner', index=index))
    return render_template('owners/add_pet.html', form=form)


@owners.route('/<int:index>/pets/<int:pet_index>/deleted')
def delete_pet_by_id(index, pet_index):
    for owner in owners_list:
        if owners_list.index(owner) == index:
            for pet in owner['pets']:
                if owner['pets'].index(pet) == pet_index:
                    del owner['pets'][pet_index]
    return redirect(url_for('owners.show_pets_by_owner', index=index))

















