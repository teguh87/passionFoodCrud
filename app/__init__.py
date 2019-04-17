from flask import Flask

app = Flask(__name__)

# Setup the app with the config.py file
app.config.from_object('app.config')

# Setup template dependancy
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

# Setup the database
from app.database import db_session, init_db, dropdb

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# dropdb()

init_db()

from app.views import main