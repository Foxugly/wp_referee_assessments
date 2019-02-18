rm db.sqlite3
rm __pycache__/*.pyc
rm assessment/__pycache__/*.pyc
rm assessment/migrations/*.py
rm assessment/migrations/__pycache__/*.pyc
rm championship/__pycache__/*.pyc
rm championship/migrations/*.py
rm championship/migrations/__pycache__/*.pyc
rm users/__pycache__/*.pyc
rm users/migrations/*.py
rm users/templatetags/__pycache__/*.pyc
rm users/migrations/__pycache__/*.pyc
python3 manage.py makemigrations users
python3 manage.py makemigrations championship
python3 manage.py makemigrations assessment
python3 manage.py migrate
python3 manage.py createsuperuser --username "test"  --email "test@test.be"
#python3 manage.py shell < data.py
python3 manage.py runserver