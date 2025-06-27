from app import app
from models import db, Plant

with app.app_context():
    print("Seeding data...")

    # Clear existing data
    Plant.query.delete()

    # Add plants
    p1 = Plant(name="Aloe", image="./images/aloe.jpg", price=11.50, is_in_stock=True)
    p2 = Plant(name="Fiddle Leaf Fig", image="./images/fig.jpg", price=25.00, is_in_stock=True)
    p3 = Plant(name="Snake Plant", image="./images/snake.jpg", price=18.00, is_in_stock=False)

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    print("Done seeding!")
