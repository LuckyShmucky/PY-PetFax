from flask import (Blueprint, render_template, request, redirect)
fact_bp = Blueprint('fact', __name__, url_prefix='/facts')

@fact_bp.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')
    
    return render_template('fact/index.html')
