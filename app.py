from distutils.command.config import config
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.config import db

app = Flask(__name__)


@app.route("/")
def home():
    return "this is a home page"

@app.route("/create", methods = ['POST'])
def create_new_pet():
    pet_data = request.json

    pet_name = pet_data['pet_name']
    pet_type = pet_data['pet_type']
    pet_age = pet_data['pet_age']
    pet_description = pet_data['pet_description']

    pet_description = pet_data['pet_description']
    pet = db.Pet(pet_name =pet_name , pet_type = pet_type, pet_age = pet_age, pet_description =pet_description )
    db.session.add(pet)
    db.session.commit()
    

    return jsonify({"success": True,"response":"Pet added"})


@app.route("/list")
def list_all_pets():
     all_pets = []
     pets = db.Pet.query.all()
     for pet in pets:
          results = {
                    "pet_id":pet.id,
                    "pet_name":pet.pet_name,
                    "pet_age":pet.pet_age,
                    "pet_type":pet.pet_type,
                    "pet_description":pet.pet_description, }
          all_pets.append(results)

     return jsonify(
            {
                "success": True,
                "pets": all_pets,
                "total_pets": len(pets),
            }
        )

@app.route("/list/<id>")
def list_user_by_id(id):
    pass

@app.route("/delete/<id>")
def delete_user(id):
    pass

if __name__ == "__main__":
    app.run(port=8080)