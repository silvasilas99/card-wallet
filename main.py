from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the app database connect URL
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.app_context().push()

# Create a router from the Flask instance object
api = Api(app)

# Create a new instance to SQLAlchemy from app
db = SQLAlchemy(app)

#TODO: Move each classes above to a single archive

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullnumber = db.Column(db.String(200), nullable=False)
    batch = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return { "fullnumber": self.fullnumber, batch: self.batch }

cardFields = {
    "id": fields.Integer,
    "fullnumber": fields.String,
    "batch": fields.String
}

class ItemImporter(Resource):
    # TODO: Create a method to read all lines from .txt file and
    # transform this data into a dic array, then insert that on database

class Items(Resource):
    @marshal_with(cardFields)
    # Find all items
    def get(self):
        return Card.query.all()
    
    # Store an item
    @marshal_with(cardFields)
    def post(self):
        data = request.json
        card = Card(fullnumber=data["fullnumber"], batch=data["batch"])
        db.session.add(card)
        db.session.commit() 

        return card

class Item(Resource):
    # Find an item by ID
    @marshal_with(cardFields)
    def get(self, pk):
        return Card.query.filter_by(id=pk).first()

api.add_resource(Items, "/")
api.add_resource(Item, "/<int:pk>")

if __name__ == "__main__":
    app.run(debug=True)