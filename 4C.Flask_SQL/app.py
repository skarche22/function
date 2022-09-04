from flask import create_app
import os

config_name=os.getenv(FLASK_CONFIG)



if __name__ =='__main__':
    app.run(debug=True)
