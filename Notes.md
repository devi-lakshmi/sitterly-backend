#For server start 
$ pipenv run uvicorn main:app --reload

#FastAPI

-> /get to get or retrieve data.
 -> /post to create Resource.
 -> /put to update a Resource.
 ->/delete to delete a Resource.

# SQLAlchemy Models

 -> Means models.py and  create a tables in DBviwer 
 ->The table name is must be in plural, while class is singular.
 
# ALEMBIC
 
 ->  Data migration tool 
 -> Every Time we create a new table or column we must genererate and upgrade
 by using this commands
 $ pipenv run alembic revision --autogenerate -m "name of the changes"
 $ pipenv run alembic upgrade head

# Pydantic Schemas
 ->we won't always be able to use the full models.
 -> Instead,we need partial models for specific use cases in which api clients need to create, update, resources etc.

# CRUD  
 ->Crud is  to create the necessary methods to work with our tables attribute.(tablesnames.py)

# APIMain
 ->set up the basic API code in main
# Git Tips
 # make sure you're on an up to date main
 $ git checkout main
 $ git pull origin main

 # then create a new branch
  $ git checkout -b feat/bookings
  Making commits:

# Making commits:
 -> Go over your changes and only stage what you need
$ git add -p

 -> Then, see what untracked files you may need to add
 $ git status

 -> Stage new files
 $ git add app/bookings.py

 -> Now commit
 $ git commit -m "feat(Bookings): Add CRUD for bookings"

 # Merging branches

 -> First, make sure everything is commited
 -> Check out main first (if you are merging TO main)
 $ git checkout main

 -> Then merge in your (feature) branch
  $ git merge feat/bookings

 ->Push it
 $ git push origin main

 -> Now you can create a new branch for the next feature!
