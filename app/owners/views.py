from flask import Blueprint, render_template, request, url_for, redirect
from app.forms import OwnerForm, PetForm, TagForm
from app.owners.models import OwnerModel, PetModel, TagModel
from app import db

owners = Blueprint('owners', __name__, template_folder='templates', static_folder='static')


@owners.route('/')
def show_owners():
    all_owners = OwnerModel.query.all()
    if not all_owners:
        return redirect(url_for('owners.add_owner'))
    return render_template('owners/show_all_owners.html', owners=all_owners)


@owners.route('/all-pets/tags', methods=['POST', 'GET'])
def show_tags():
    all_tags = TagModel.query.all()
    form = TagForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['name']
        tag = TagModel(name=name)
        if TagModel.query.filter_by(name=name).first():
            return render_template('owners/show_all_tags.html', tags=all_tags, form=form)
        db.session.add(tag)
        db.session.commit()
    return render_template('owners/show_all_tags.html', tags=all_tags, form=form)


@owners.route('/add_owner', methods=['POST', 'GET'])
def add_owner():
    form = OwnerForm(request.form)
    if request.method == 'POST' and form.validate():
        owner = OwnerModel(name=request.form['name'].lower(), age=request.form['age'], location=request.form['location'].lower())
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for('owners.show_owners'))
    return render_template('owners/add_owner.html', form=form)


@owners.route('/<int:owner_id>/edit', methods=['POST', 'GET'])
def edit_owner(owner_id):
    form = OwnerForm(request.form)
    current_owner = OwnerModel.query.get(owner_id)
    if request.method == 'POST' and form.validate():
        current_owner = OwnerModel.query.filter_by(id=owner_id).update({'name': request.form['name'].lower(), 'age': request.form['age'], 'location': request.form['location'].lower()})
        db.session.commit()
        return redirect(url_for('owners.show_owners'))
    return render_template('owners/edit_owner.html', owner=current_owner, form=form)


@owners.route('all_pets/<int:pet_id>/edit', methods=['POST', 'GET'])
def edit_pet(pet_id):
    form = PetForm(request.form)
    current_pet = PetModel.query.get(pet_id)
    if request.method == 'POST' and form.validate():
        updated_pet = PetModel()
        for item in request.form.lists():
            if item[0] == 'name':
                updated_pet.name = item[1][0]
            if item[0] == 'age':
                updated_pet.age = item[1][0]
            if item[0] == 'type_pet':
                updated_pet.type_pet = item[1][0]
            else:
                for tag_name in item[1]:
                    tag = TagModel.query.filter(TagModel.name==tag_name).first()
                    updated_pet.tags.append(tag)
        current_pet = PetModel.query.filter_by(id=pet_id).update({'name': updated_pet.name.lower(), 'age': updated_pet.age, 'type_pet': updated_pet.type_pet.lower()})
        db.session.commit()
        return redirect(url_for('owners.show_all_pets'))
    return render_template('owners/edit_pet.html', pet=current_pet, form=form)


@owners.route('/<int:index>/pets/add_pet', methods=['GET', 'POST'])
def add_pet(index):
    form = PetForm(request.form)
    if request.method == 'POST' and form.validate():
        print(request.form)
        pet = PetModel()
        for item in request.form.lists():
            if item[0] == 'name':
                pet.name = item[1][0].lower()
            if item[0] == 'age':
                pet.age = item[1][0]
            if item[0] == 'type_pet':
                pet.type_pet = item[1][0].lower()
            else:
                for tag_name in item[1]:
                    tag = TagModel.query.filter(TagModel.name == tag_name).first()
                    pet.tags.append(tag)
        pet.owner_id = index
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('owners.show_pets_by_owner', index=index))
    return render_template('owners/add_pet.html', form=form)


@owners.route('/<int:index>/pets')
def show_pets_by_owner(index):
    pets_of_owner = PetModel.query.filter_by(owner_id=index).all()
    owner = OwnerModel.query.filter_by(id=index)
    if not pets_of_owner:
        return redirect(url_for('owners.add_pet', index=index))
    return render_template('owners/show_pets_of_owner.html', owner=owner, pets=pets_of_owner, index=index)


@owners.route('/all_pets')
def show_all_pets():
    all_pets = PetModel.query.all()
    if not all_pets:
        return redirect(url_for('owners.add_owner'))
    return render_template('owners/show_all_pets.html', pets=all_pets)


@owners.route('/<string:type_pet>')
def show_owners_by_pet_type(type_pet):
    pets_of_this_type = PetModel.query.filter_by(type_pet=type_pet).all()
    owners_with_pet_type = []
    for pet in pets_of_this_type:
        owners_with_pet_type.append(OwnerModel.query.filter_by(id=pet.owner_id).first())
    return render_template('owners/show_owners_by_pet_type.html', owners=owners_with_pet_type, type_pet=type_pet)


@owners.route('/<int:owner_id>/deleted')
def delete_owner(owner_id):
    user = OwnerModel.query.filter_by(id=owner_id).first()
    pets = PetModel.query.filter_by(owner_id=owner_id).all()
    db.session.delete(user, pets)
    db.session.commit()
    return redirect(url_for('owners.show_owners'))


@owners.route('/all_pets/<int:pet_index>/deleted')
def delete_pet_by_id(pet_index):
    pet = PetModel.query.filter_by(id=pet_index).first()
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('owners.show_all_pets'))


@owners.route('/all_pets/<string:type_pet>')
def show_all_pets_by_type(type_pet):
    pets_by_type = PetModel.query.filter_by(type_pet=type_pet).all()
    count = len(pets_by_type)
    if not pets_by_type:
        return redirect(url_for('owners.add_owner'))
    return render_template('owners/show_all_pets_by_type.html', pets=pets_by_type, type_pet=type_pet, count=count)





