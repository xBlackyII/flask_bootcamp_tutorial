from app import db, Puppy

# CREATE
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# READ
