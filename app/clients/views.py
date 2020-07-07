from flask import Blueprint, render_template, request, url_for, redirect
from app.forms import ClientForm, PetForm
from app.clients_list import clients_list
from app.pets_list import pets_list

clients = Blueprint('clients', __name__, template_folder='templates', static_folder='static')


@clients.route('/')
def main_cl():
    return render_template('clients/index_cl.html', clients=clients_list, pets = pets_list)


@clients.route('/new/', methods=['POST', 'GET'])
def new_cl():
    form = ClientForm()
    name = ''
    age = 0
    location = ''
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        location = request.form['location']
        clients_list.append({'id': len(clients_list)+1, 'name': name, 'age': age, 'location': location})
        return render_template('index.html')
    return render_template('clients/new_cl.html', name=name, age=age, location=location, form=form)


@clients.route('/<id_cl>/')
def about_cl(id_cl):
    owner = None
    pets = []
    for client in clients_list:
        if str(client.get('id')) == id_cl:
            owner = client
    for pet in pets_list:
        if pet.get('userId') == owner.get('id'):
            pets.append(pet)

    return render_template('clients/about_cl.html', client=owner, pets=pets)





