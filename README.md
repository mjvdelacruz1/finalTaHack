# finalTaHack
Step 1:
Run virtual environment
- In the root folder
- .\venv\Scripts\activate

Step 2:
- Install Django and Django Compressor
- pip install Django django-compressor

Step 3:
- Install pytailwindcss
- pip install pytailwindcss

Step 4:
- Check if tailwindcss has logged in successfully
- tailwindcss

Step 5:
- Run tailwindcss
- tailwindcss -i ./static/src/main.css -o ./static/src/output.css --minify --watch

Step 6:
- Run Server
- python manage.py runserver
