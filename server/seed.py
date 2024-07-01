#!/usr/bin/env python3
# server/seed.py

from faker import Faker
from random import choice as rc
from app import app
from models import db, Pet

def seed_data():
    # Use Flask application context to ensure database operations work correctly
    with app.app_context():
        # Uncomment the following lines if you want to drop and recreate all tables
        # This can be useful in a development environment to reset the database state
        # db.drop_all()
        # db.create_all()

        fake = Faker()  # Create a Faker instance to generate fake data
        Pet.query.delete()  # Delete all existing rows in the "pets" table
        print("Seeding pets...")  # Inform user that seeding has started

        pets = []  # Initialize an empty list to hold Pet instances

        species = ['Dog', 'Cat', 'Hamster', 'Snake']  # List of species for random selection

        # Generate 30 Pet instances with random names and species
        for _ in range(30):
            pet = Pet(name=fake.first_name(), species=rc(species))
            pets.append(pet)  # Add each Pet instance to the list
        
        # Add all Pet instances to the session and commit to the database
        db.session.add_all(pets)
        db.session.commit()

        print("Seeding complete!")  # Inform user that seeding has finished

# Execute the seed_data function to perform the seeding
seed_data()
