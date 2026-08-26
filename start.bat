@echo off
call env\Scripts\activate
cd osspboom
python manage.py runserver
pause