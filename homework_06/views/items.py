from flask import Blueprint, render_template

items_app = Blueprint(
    "items_app",
    __name__,
    # url_prefix="/items"
)


@items_app.get("/", endpoint="list")
def items_list():
    return render_template("items/list.html")


@items_app.get("/<int:item_id>/", endpoint="details")
def items_detail(item_id: str):
    return {
        "data": {
            "id": item_id,
            "name": "single",
        },
    }


@items_app.post("/")
def create_tem():
    return {}


@items_app.get("/next-item/", endpoint="next-item")
def get_next_item_page():
    return render_template("items/next-item.html")
