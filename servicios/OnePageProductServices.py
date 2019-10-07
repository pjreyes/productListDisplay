from flask_restful import Resource, Api, abort,reqparse
from flask import jsonify, request
import json

class OnePageProduct(Resource):
    def get(self): 
# 		if request.args.get('Id') is None:
# 			response = {
#   "errors":[
# 	  "invalid ID"
#   ]}
# 			return response 
        response = {
  "errors":[
 
  ],
  "success":"true",
  "products":[
     {
        "product":{
           "brand":"Samsung",
           "displayName":"Smartphone Galaxy J5 Prime Negro Dual",
           "id":"1494243",
           "prices":[
              {
                 "label":"Internet",
                 "originalPrice":"56.981",
                 "symbol":"$",
                 "type":3,
                 "isLoyalty":"false"
              },
              {
                 "label":"Normal",
                 "originalPrice":"56.990",
                 "symbol":"$",
                 "type":2,
                 "isLoyalty":"false"
              },
              {
                 "label":"CMR Puntos",
                 "originalPrice":"379",
                 "type":14,
                 "isLoyalty":"false"
              }
           ],
           "published":"true",
           "url":"/product/5527259/Smartphone-Galaxy-J5-Prime-Negro-Dual/5527259",
		   "description":"BLABLABLA BLA BLA BLA BLA blablabla"
        }
     }
  ]
}
	    print(response)
            
        return response


# ----------------
# import requests
# from bs4 import BeautifulSoup

# url = "https://articulo.mercadolibre.cl/MLC-463906296-skis-atomic-expert-hv-series-6-con-fijaciones-_JM"
# page = requests.get(url)

# # print(page.status_code)

# # print(page.content)

# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup.prettify())

# print(soup)
