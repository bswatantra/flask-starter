from flask import Blueprint, request, render_template, redirect, url_for

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

    return render_template('user/index.html')


@bp.route("<int:id>")
def show(id):
    return render_template('user/show.html', id=id)
