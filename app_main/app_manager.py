from app_main import create_app
from flask_script import Server, Manager
# Here we define the extension of flask to flask-script
app = create_app()
manager = Manager(app)
manager.add_command("runserver", Server(host='0.0.0.0', port=5000, use_debugger=True))

# In this script we call all in a context manager of @flask-script libraries
# Here we call the executable part of the app with manager
if __name__ == '__main__':
    manager.run()