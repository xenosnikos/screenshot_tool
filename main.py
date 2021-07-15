from flask import Flask
from flask_restful import Api

from controllers.screenshot import ScreenShot

app = Flask(__name__)
api = Api(app)

api.add_resource(ScreenShot, "/v2/screenShot")

if __name__ == "__main__":
    app.run()
