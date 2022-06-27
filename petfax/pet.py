from flask import Blueprint, render_template
import json
pets = json.load(open('pets.json'))

bp = Blueprint(
    'pet',
    __name__
)

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)
# @bp.route('/:id')
# def show_page():
#     return render_template('show_page.html', pets=pets )
