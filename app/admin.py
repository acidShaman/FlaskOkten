from flask import redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, LoginManager
from app import app, db
from app.owners.models import UserModel, PetModel, OwnerModel, TagModel


class FixedModelView(ModelView):
    form_excluded_columns = 'pets'


class SecureModelView(FixedModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


admin = Admin(app)
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)


admin.add_view(SecureModelView(UserModel, db.session))
admin.add_view(FixedModelView(OwnerModel, db.session))
admin.add_view(FixedModelView(PetModel, db.session))
admin.add_view(FixedModelView(TagModel, db.session))

