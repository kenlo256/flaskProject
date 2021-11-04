from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return "NORTH KOREA NUMBER ONE"

    def post(self):
        return "Posted:"


api.add_resource(HelloWorld, "/hello")

if __name__ == '__main__':
    app.run()
