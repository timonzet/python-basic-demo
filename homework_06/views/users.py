import json
from select import select

import requests
from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash
from werkzeug.exceptions import NotFound

from models import db, User
from .forms.users import UserForm
from jsonplaceholder_requests import fetch_users_data


users_app = Blueprint(
    "users_app",
    __name__,
    url_prefix="/users",
)


@users_app.get("/", endpoint="list")
def get_user_list():
    users: list[User] = User.query.order_by(User.id).all()
    return render_template("users/list.html", users=users)


def get_user_by_id(user_id: int) -> User:
    return User.query.get_or_404(
        user_id,
        description=f"Product #{user_id} not found!",
    )


@users_app.get("/<int:user_id>/", endpoint="details")
def get_user_details(user_id: int):
    user: User | None = get_user_by_id(user_id=user_id)
    if user is None:
        raise NotFound(f"User #{user_id} not found!")

    return render_template("users/details.html", user=user)


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_new_user():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("users/add.html", form=form), 400

    user = User(name=form.data["name"], username=form.data["username"])
    users1 = User.query.order_by(User.id).all()
    users_list = [user.username for user in users1]
    if user.username not in users_list:
        db.session.add(user)
        db.session.commit()
        url = url_for("users_app.details", user_id=user.id)
        flash(f"Created user {user.name!r}", category="success")
        return redirect(url)
    else:
        flash(f"Это имя занято {user.username!r}", category="warning")
        return render_template("users/add.html", form=form), 400

    # flash(f"Created product {product.name!r}")


@users_app.route(
    "/<int:user_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
def confirm_delete_product(user_id: int):
    user = get_user_by_id(user_id=user_id)
    if request.method == "GET":
        return render_template("users/confirm-delete.html", user=user)
    user_name = user.username
    db.session.delete(user)
    db.session.commit()
    flash(f"Deleted user {user_name!r}", category="warning")
    url = url_for("users_app.list")

    return redirect(url)


@users_app.route("/", methods=["POST"])
def create_users():
    users_data = fetch_users_data()
    users1 = User.query.order_by(User.id).all()
    users_list = [user.username for user in users1]
    users = User.query.with_entities(User.username == "Artem")
    print(users)
    # print(users1)
    for user in users_data:
        if user["username"] not in users_list:
            # order_by(User.id).all():
            print(user)
            new_user = User(
                name=user["name"],
                username=user["username"],
                email=user["email"],
            )
            flash(f"Created user {user.name}", category="success")
            db.session.add(new_user)
            db.session.commit()
        else:
            continue

    url = url_for("users_app.list")

    return redirect(url)
