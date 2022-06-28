from flask import (Blueprint, flash, render_template, request, redirect)
from . import models
fact_bp = Blueprint('fact', __name__, url_prefix='/facts')

@fact_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']
        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()
        # print(request.form, flush=True)
        return redirect('/facts')
    results = models.Fact.query.all()
    return render_template('fact/index.html', facts=results)
