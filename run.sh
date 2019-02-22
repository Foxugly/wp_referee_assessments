python3 manage.py makemigrations customuser
python3 manage.py makemigrations championship
python3 manage.py makemigrations assessment
python3 manage.py migrate
python3 manage.py createsuperuser --username "test"  --email "test@test.be"
#python3 manage.py shell < data.py
python3 manage.py runserver