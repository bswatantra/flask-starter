from flask import Blueprint, request, render_template, redirect, url_for
from app.models.user import User as UserModel
from app.extentions import db

bp = Blueprint(
    'users',
    __name__,
    url_prefix='/users'
)


@bp.route("")
def index():
    users = UserModel.query.all()
    return render_template('user/index.html', users=users)


@bp.route("create")
def create():
    return render_template('user/create.html')


@bp.route('', methods=["POST"])
def store():
    user = UserModel(
        name=request.form["name"],
        email=request.form["email"]
    )
    db.session.add(user)

    db.session.commit()


@bp.route("<int:id>", methods=["GET"])
def show(id):
    return render_template('user/show.html', id=id)


@bp.route("<int:id>", methods=["PUT"])
def update(id):
    return render_template('user/show.html', id=id)


@bp.route("<int:id>", methods=["DELETE"])
def destroy(id):
    user = UserModel.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users.index'))
