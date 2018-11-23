import logging
from flask_restful_swagger_2 import Resource, swagger
from net.route.SwaggerSchema import *
from commons.Common import Common


class GetPelple(Resource):
    @swagger.doc({
        'tags': ['PeopleAPI'],
        'description' : '取得人員清單',
        'responses' :{
            '200' : {
                'description' : '顯示人員清單',
                'schema' : PeopleList_RModel,
                'examples' : {
                    'application/json' : {
                        'code' : 0,
                        'msg' : '',
                        'datas' : [
                            {
                                "fname": "Kent",
                                "lname": "Brockman",
                                "timestamp": "2018-11-05 23:35:43"
                            },
                            {
                                "fname": "Bunny",
                                "lname": "Easter",
                                "timestamp": "2018-11-05 23:35:43"
                            },
                            {
                                "fname": "Doug",
                                "lname": "Farrell",
                                "timestamp": "2018-11-05 23:35:43"
                            }
                        ]
                    }
                }
            }
        }
    })
    def get(self):
        """ 取得人員清單"""
        logging.getLogger('PeopleApi').info(self.__class__.__name__ + ' get')

        PEOPLE = [
            {
              "Name": "Farrell",
              "Inform": {
                "fname": "Doug",
                "lname": "Farrell",
                "timestamp": "232"
              }
            },
            {
              "Name": "Brockman",
              "Inform": {
                "fname": "Kent",
                "lname": "Brockman",
                "timestamp": "232"
              }
            },
            {
              "Name": "Easter",
              "Inform": {
                "fname": "Doug",
                "lname": "Farrell",
                "timestamp": "232"
              }
            }
          ]

        # response code from ReturnCode and message
        return Common.response(0, data=PEOPLE)

