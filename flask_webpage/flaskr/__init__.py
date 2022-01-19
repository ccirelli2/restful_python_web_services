import os
from flask import Flask

def create_app(test_config=None):
    # Create & Configure the App
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'))

    if test_config is None:
        # Load the instance confif it it exists when not testing
        app.config.from_py_file(test_config)

    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass


    print('App instance path => {}'.format(app.instance_pathi))

create_app()
