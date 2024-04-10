# Dynamic EasyAlgo - e-learing plateform free of cost all resources

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


![Screenshot 2024-04-08 173253](https://github.com/surajbhan93/easyalgo/assets/114743961/583bb5de-8f10-42c1-89f3-b50b29d3edc7)

## Introduction
**"Dynamic EasyAlgo"** is a developer blog and portfolio website built using **Django** and **Tailwind CSS**. It includes several pages such as Home, About, Contact, Blog, Projects, Categories, and custom 404 pages. The project features a clean and modern design that is fully responsive and optimized for performance. It includes a powerful admin interface for managing the content, and is easy to customize and deploy to a production environment.

![EasyAlgo](https://github.com/surajbhan93/easyalgo/assets/114743961/5fef49f6-fded-4f90-8548-7ad03bd14dc7)

## Table of Content
  * [Introduction](#introduction)
  * [Installation](#installation)
  * [Technologies Used](#technologies-used)
  * [Features](#features)
  * [Pages](#pages)
  * [Website Screenshots](#website-screenshots)
  * [Admin Screenshots](#admin-screenshots)
  * [Deployment](#deployment)
  * [Conclusion](#conclusion)
  
## Installation
1. Clone the repository:
```
git clone https://github.com/ashish-makes/django-tailwind-blog.git
```
2. Navigate to the project directory:
```
cd `django-tailwind-blog`
```
3. Create and activate a new virtual environment:
```
python -m venv env
source env/bin/activate
```
4. Install the project dependencies:
```
pip install -r requirements.txt
```
5. Install the `django-tailwind` module:
```
pip install django-tailwind
```
6. Add `tailwind` to your `INSTALLED_APPS` list in `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'tailwind',
    # ...
]
```
7. Run the Tailwind CSS configuration command:
```python
python manage.py tailwind init
```
8. Create the database tables:
```python
python manage.py migrate
```
9. Run the development server:
```python
python manage.py runserver
```

## Technologies used
1. HTML
2. CSS
3. JavaScript
4. Python

### Primary Modules used
1. Django==4.1.4
2. django-tailwind==3.4.0
3. whitenoise==6.3.0
4. psycopg2==2.9.5
5. django-tinymce==3.5.0

## Features
1. Responsive design using Tailwind CSS
2. Admin dashboard for managing blog posts and portfolio items
3. Contact form for sending messages to the site owner

## Pages
- `Home`: The landing page of the website, which displays a brief introduction and links to other pages.
- `About`: A page that provides information about the site owner, their background, and skills.
- `Contact`: A page that contains a contact form for visitors to send messages to the site owner.
- `Blog`: A page that displays a list of blog posts in reverse chronological order, with links to individual post pages.
- `Blog Post`: A page that displays the content of a single blog post, including the title, author, date, and content.
- `Projects`: A page that displays a list of portfolio projects, with links to individual project pages.
- `Project`: A page that displays the details of a single portfolio project, including the title, description, date, and any relevant images or links.
- `Categories`: A page that displays a list of blog post categories, with links to filtered lists of posts for each category.
- `Custom 404 Pages`: Custom error pages that display when a user navigates to a non-existent page or encounters an error.

## Website Screenshots

![Screenshot 2024-04-09 071839](https://github.com/surajbhan93/easyalgo/assets/114743961/a4a6b889-3b6d-490d-b763-27c0ea43e14e)


![Screenshot 2024-04-09 071907](https://github.com/surajbhan93/easyalgo/assets/114743961/5eb1b4a7-d3ca-41be-8a03-2fefdd3438b1)

![Screenshot 2024-04-09 071925](https://github.com/surajbhan93/easyalgo/assets/114743961/e0c435f3-6d67-44eb-9687-71f1352e07b5)

![Screenshot 2024-04-09 071940](https://github.com/surajbhan93/easyalgo/assets/114743961/214c15de-210e-455d-85a4-ada0e96b3e66)

![Screenshot 2024-04-09 071957](https://github.com/surajbhan93/easyalgo/assets/114743961/e2201f84-4a51-4be4-820d-a802f52f7a5f)

![Screenshot 2024-04-09 072016](https://github.com/surajbhan93/easyalgo/assets/114743961/961713b1-0191-4f2e-9122-8bde2e7176c5)

![Screenshot 2024-04-09 072032](https://github.com/surajbhan93/easyalgo/assets/114743961/a2de8933-02a6-4b0a-9729-bb70e9b6364e)

![Screenshot 2024-04-09 072056](https://github.com/surajbhan93/easyalgo/assets/114743961/3f27724c-a2a3-47ba-8f5e-0b3bf873c802)

![Screenshot 2024-04-09 072120](https://github.com/surajbhan93/easyalgo/assets/114743961/ac77c706-1ede-4d5a-82e8-03a21f42c0c4)

![Screenshot 2024-04-09 072135](https://github.com/surajbhan93/easyalgo/assets/114743961/d37fbed7-c181-471c-9c55-3a6462e44a74)

## Admin Screenshots
![Screenshot 2024-04-10 194047](https://github.com/surajbhan93/easyalgo/assets/114743961/ade8a632-1fb7-4d98-ac06-c71ad1ae5629)



## Deployment![Screenshot 2024-04-10 194056](https://github.com/surajbhan93/easyalgo/assets/114743961/8a42f94e-2d9a-4b94-b293-fffcbc08cc22)

![Screenshot 2024-04-10 194122](https://github.com/surajbhan93/easyalgo/assets/114743961/4f0b1ee8-7404-4f97-b497-f82d4a57cd1c)



![Screenshot 2024-04-10 194158](https://github.com/surajbhan93/easyalgo/assets/114743961/ee452849-8fbb-44e1-a524-d13f71a99d9a)

To deploy this project to a web server, you can follow these general steps:


1. Set up a web server that can run Python applications. This could be a VPS, a PaaS like Heroku, or a cloud-based server like AWS.
2. Clone the repository to your server:
```
git clone https://github.com/ashish-makes/django-tailwind-blog.git
```
3. Install the project dependencies on your server using `pip`:
```
pip install -r requirements.txt
```
4. Set up a database for the project, if necessary. You can use a database like PostgreSQL, MySQL, or SQLite, depending on your needs.
5. Configure the settings.py file with your server's settings:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = '/var/www/static/'
MEDIA_ROOT = '/var/www/media/'

ALLOWED_HOSTS = ['example.com', 'www.example.com']
```
The DATABASES setting specifies the database connection details. In this example, we're using PostgreSQL with a database named `mydatabase`, a user named `mydatabaseuser`, and a password of `mypassword`. The `STATIC_ROOT` and `MEDIA_ROOT` settings specify the file paths where static files and media files will be stored. The `ALLOWED_HOSTS` setting is a list of domain names that the application is allowed to serve.
6. Run the python manage.py collectstatic command to collect all the static files into the STATIC_ROOT directory:
```python
python manage.py collectstatic
```
7. Start the Django development server, or set up a production server using a WSGI server like uWSGI or Gunicorn.
```python
python manage.py runserver
```
8. Access the website using your server's IP address or domain name, and the port number of the server if necessary. For example, if you're running the development server on port 8000, you can access the website at `http://your-server-ip:8000/`.
