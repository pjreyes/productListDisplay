from flask import Flask, request, Response
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
import logging
import sys
import json
from servicios.ProductListDisplayServices import ProductListDisplay

sys.path.append('../')


app = Flask(__name__)
api = Api(app)


api.add_resource(ProductListDisplay,'/api/v1/ProductListDisplay')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port='5004')
