from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from models import db, Plant

app = Flask(__name__)

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///plants.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init
db.init_app(app)
migrate = Migrate(app, db)

# Routes
@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants])

@app.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = Plant.query.get_or_404(id)
    data = request.get_json()

    if 'is_in_stock' in data:
        plant.is_in_stock = data['is_in_stock']

    db.session.commit()
    return jsonify(plant.to_dict())

@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    db.session.delete(plant)
    db.session.commit()
    return make_response('', 204)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
