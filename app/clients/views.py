from flask import Blueprint, render_template, request, url_for, redirect
from app.forms import ClientForm
from app.clients_list import clients_list

clients = Blueprint('clients', __name__, template_folder='templates', static_folder='static')


@clients.route('/')
def main_cl():
    return render_template('clients/index_cl.html', clients=clients_list)


@clients.route('/new/', methods=['POST', 'GET'])
def new_cl():
    form = ClientForm()
    name = ''
    age = 0
    location = ''
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        location = request.form['location']
        clients_list.append({'id': len(clients_list)+1, 'name': name, 'age': age, 'location': location, 'pets': []})
        return redirect(url_for('clients.main_cl'))
    return render_template('clients/new_cl.html', name=name, age=age, location=location, form=form)


@clients.route('/client/<id_cl>')
def about_cl(id_cl):
    for i in clients_list:
        if i.get('id') == id_cl:
            client = i
    return render_template('clients/about_cl.html', client=client)
