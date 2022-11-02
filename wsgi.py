import os


from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from config import DevelopementConfig, ProductionConfig

# creating an application instance
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or DevelopementConfig)

# initializes extensions
toolbar = DebugToolbarExtension(app)

import views

if __name__ == "__main__":
    app.run()