You need to install Microsoft Visual C++ 14.0 
pip install httptools
pip install fastapi[all]
pip install SQLAlchemy   #database orm
pip install alembic   #database migration tool


uvicorn main:app --reload
uvicorn app.main:app --reload

alembic init alembic
alembic revision -m "create posts table"
alembic upgrade {revision number}
alembic current
alembic heads #see lates revision
alembic upgrade head
alembic downgrade
alembic downgrade -1 #downgrade back 1 version
alembic revision --autogenerate -m "auto-vote"

pip freeze > requirements.txt
pip install -r requirements.txt