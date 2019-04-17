# Wellcome
Hai this application using flask application framework framework is pre-configured with Flask-SQLAlchemy,Flask-WTF, Fabric, Coverage, and the Bootstrap frontend (among others). This will get your Flask app up and running by using docker or docker-compose orchestrating.

**This is very simple program based on what it's request**

#Project Structure
```
├── database.py
├── app.py
├── config.py
├── Dockerfile # docker configuration
├── models.py
├── requirements.txt
├── static
│   ├── css
│   │   ├── custom.css
└── templates
|    ├── index.html
|    ├── layout.html
|    ├── show.html
|    ├── form.html
|___ mixins
|    ├── mixins.py
|___ forms
|    ├── forms.py
|___ views
|    ├── views.py
   
```

# Containers docker structure
![alt text](https://github.com/mrsan22/Angular-Flask-Docker-Skeleton/blob/master/project_architecture.png)

# How to run
**NOTE**: *Make sure you have Docker here.*

Clone this repository
Then navigate back and execute following commands:
> docker-compose build
> docker-compose up
> OR just run one command: docker-compose -f docker-compose.yml up --build
Open Browser and type following URL:
localhost - It should display index page a default message from backend list of record.
localhost/add - It should display add form.
localhost/show - Showed detail record.
This seed project is good for starting up with any Flask-WTF-Docker project, so check it out and feel free to fork, update, plug in your project etc. Let me know if you find any issues.

`docker-compose build # for built the dependancies`
`docker-compose up # for run all container`
`docker-compose down # for kill all live container`

# References/Credits
Docker team and blog has wrote some tutorial for help me build this app and finished the hiring test