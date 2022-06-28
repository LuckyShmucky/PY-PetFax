from flask import Flask 
from flask_migrate import Migrate

def create_app(): 
    app = Flask(__name__)
    # app.run(debug=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Wishingwell999!@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    
    from . import pet
    app.register_blueprint(pet.bp, url_prefix="/pets")

    from . import show
    app.register_blueprint(show.bp2, url_prefix='/pets/<int:id>')

    from . import new_fact_form
    app.register_blueprint(new_fact_form.form_bp, url_prefix='/facts/new')
    
    from . import fact 
    app.register_blueprint(fact.fact_bp)

    return app
