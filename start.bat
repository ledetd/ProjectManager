@echo off

:start
cls
set mypath=%cd%
@echo %mypath%

cd %mypath%
call venv\Scripts\activate.bat

@echo Starting server and Opening browser...
timeout /t 0 /nobreak

start "" http://127.0.0.1:8000/
start python manage.py runserver 8000
pause
exit