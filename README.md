# Group 48

- [ ] Check that all links are inserted
- [ ] Check that all commands are correct

This is the code repo for group 48 in the subject TDT4140 Software Engineering.

Routines and standards for **contributing** can be found [here](#).

## Team Members
- Magnus Stavland Jakobsen, magnsjak@stud.ntnu.no
- Andreas Granhøy-Lieng, andrgran@stud.ntnu.no
- Iver Ringheim, iverri@stud.ntnu.no
- Mats Kjær, mbkjaer@stud.ntnu.no
- Aksel Lessum, akselhl@stud.ntnu.no
- Ksenia Mordovets, kseniam@stud.ntnu.no

## Technology and Framework (unfinished)

**Back-end:**

[Python 3.9.6](https://www.python.org/downloads/): Is the chosen language

[Django 3.2.8](https://www.djangoproject.com): Web-framework written in Python, is used to host all pages

**Front-end:**

[Bootstrap ?version?](https://getbootstrap.com/docs/4.1/getting-started/introduction/): 

?[Crispy-forms#](https://github.com/django-crispy-forms/django-crispy-forms):?
?[Pillow#](https://python-pillow.org)?

## Installation 

1. Download [git](https://git-scm.com/downloads) if not already installed.
2. Clone the project with the following command from inside the folder where you want the project:
`git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2023/landsby-3/gruppe-48/pu48.git`
3. Make sure you have the [required](#technology-and-framework) version of Python installed.
4. Install dependencies from inside `pu48/Toolio/`: `pip install -r requirements.txt`
5. In order to create and apply the database schema run the following commands from inside `pu48/Toolio/`:
`python manage.py makemigrations`
`python manage.py migrate`
6. Run the server:
`python manage.py runserver`
7. Go to:
[http://localhost:8000/](http://localhost:8000/)

## Maintenance

### Reset the Database

1. `cd ./pu48/Toolio`
2. `python manage.py flush` answer 'yes' if asked whether you're sure about resetting

### Make a New SuperUser

1. `cd ./pu48/Toolio`
2. `python manage.py createsuperuser`
3. Finish registration by filling out the questions asked in the terminal

## Testing

This project has only used unit-testing. To run all the test type the following command:
`python manage.py test ?Toolio?`

### Test-coverage

1. `pip install coverage`
2. To get a coverage report in the terminal: `coverage run --source='#' manage.py test && coverage report` replace the '#' with one of the following: main, Toolio, user
3. To also get a html coverage report: `coverage run --source='#' manage.py test && coverage report && coverage html` replace the '#' with one of the following: main, Toolio, user
4. To open the html report 'live server' can be used, if not already installed run: `npm i -g live-server` and then to open the report run: `cd htmlcov/ && live-server`

## Not finished -->

## Roadmap

**If you have ideas for releases in the future, it is a good idea to list them in the README.**

## Contributing

**State if you are open to contributions and what your requirements are for accepting them.
For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.
You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.**

**Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.**

**Please make sure to update tests as appropriate.**

## License

**[MIT](https://choosealicense.com/licenses/mit/)**

