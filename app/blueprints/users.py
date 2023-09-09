from flask import Blueprint, request, render_template, redirect, url_for
from app.models.user import User as UserModel

bp = Blueprint(
    'users',
    __name__,
    url_prefix='/users'
)


@bp.route("", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # store user data in db
        user = request.form

        return redirect(url_for('users.index'))
    users = UserModel.query.all()
    return render_template('user/index.html', users=users)


@bp.route("<int:id>")
def show(id):
    return render_template('user/show.html', id=id)
