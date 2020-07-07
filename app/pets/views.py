from flask import Blueprint, render_template, request, url_for, redirect
from app.forms import PetForm
from app.pets_list import pets_list
from app.clients_list import clients_list

pets = Blueprint('pets', __name__, template_folder='templates', static_folder='static')


@pets.route('/')
def main_p():
    return render_template('pets/index_p.html', pets=pets_list)


@pets.route('/<pet_type>')
def show_cl_w_pet(pet_type):
    clients_with_pettype = []
    for pet in pets_list:
        if pet.get('type_pet') == pet_type:
            for client in clients_list:
                if pet.get('userId') == client.get('id'):
                    clients_with_pettype.append(client)
    return render_template('pets/clients_w_spec_pets.html', clients=clients_with_pettype, type=pet_type)


@pets.route('/add_pet', methods=['POST', 'GET'])
def add_pet():
    form = PetForm()
    name = ''
    age = 0
    type_pet = ''
    client_id = ''
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        type_pet = request.form['type_pet']
        client_id = int(request.form['client_id'])
        for client in clients_list:
            if client.get('id') == client_id:
                pets_list.append({'userId': client_id, 'id': len(pets_list)+1, 'name': name, 'age': age, 'type_pet': type_pet})
        return render_template('index.html')
    return render_template('pets/add_pet.html', name=name, age=age, type=type_pet, client_id=client_id, form=form)


@pets.route('/delete/<pet_name>', methods=['POST', 'GET'])
def delete_pet(pet_name):
    if request.method == 'GET':
        for pet in pets_list:
            if pet.get('name') == pet_name:
                pets_list.remove(pet)
    return render_template('pets/delete_pet.html', pet_name=pet_name)


@pets.route('/count/<type_pet>')
def count_species(type_pet):
    counter = 0
    for pet in pets_list:
        if pet.get('type_pet') == type_pet:
            counter += 1
    return render_template('pets/count_pet.html', type_pet=type_pet, counter=counter)


