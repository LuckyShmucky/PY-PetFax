from flask import Flask 


def create_app(): 
    app = Flask(__name__)
    # app.run(debug=True)
    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    
    from . import pet
    app.register_blueprint(pet.bp, url_prefix="/pets")

    from . import show
    app.register_blueprint(show.bp2, url_prefix='/pets/<int:id>')

    from . import new_fact_form
    app.register_blueprint(new_fact_form.form_bp, url_prefix='/facts/new')
   
    return app
