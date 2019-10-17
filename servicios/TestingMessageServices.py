

from flask_restful import Resource, Api, abort,reqparse
from flask import jsonify, request
import json

class TestingMessage(Resource):
    def get(self):    
        response ={
        "Status_code":200,
        "Body":[
		              {
		                 "id":1,
		                 "Theme":"K8S",
		                 "Rating":"3",
		                 "Message":"genial"
		              },
		              {
		                 "id":2,
		                 "Theme":"K8S",
		                 "Rating":"1",
		                 "Message":"Horrible"
		              }
        ]
        }
        
        print(response)
            
        return response


