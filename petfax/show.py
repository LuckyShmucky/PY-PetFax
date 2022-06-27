from flask import (Blueprint, render_template)
import json
pets = json.load(open('pets.json'))
bp2 = Blueprint(
    'show', 
    __name__
)

@bp2.route('/')
def show(id):
    return render_template('show.html', pet=pets[id-1])