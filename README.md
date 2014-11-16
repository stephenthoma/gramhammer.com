# Flask Jumpstart

Fork of natehefner's skeleton application with some *very opinionated* changes.
Enables quickly starting development of web-applications with a
[Flask](http://flask.pocoo.org) + [Angular](http://angularjs.org) stack.

## Extensions

* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.org/en/latest/)
* [Flask-Mail](http://pythonhosted.org/flask-mail/)

## Installation
Instructions for getting up and running in an OS X environment with
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)

Clone the project:

```
git clone https://github.com/sthoma/flask-jumpstart.git
```

Set up a virtual environment:

```
cd flask-jumpstart
mkvirtualenv jumpstart
```

Install requirements:

```
pip install -r requirements/dev.txt
```

Run the development webserver:

```
python manage.py runserver
```

View it in your browser:

```
http://localhost:5000
```

## Testing
Tests for the Flask backend can be run using:

```
python manage.py test [--coverage]
```

## License

* No Warranty Expressed or Implied. Sofware is as is.
* [MIT License](http://opensource.org/licenses/mit-license.php)
