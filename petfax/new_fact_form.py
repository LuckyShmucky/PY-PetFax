from flask import Blueprint, render_template
form_bp = Blueprint('new_fact_form', __name__)

@form_bp.route('/')
def form():
    return render_template('fact/new_fact_form.html')