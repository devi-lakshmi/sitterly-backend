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

