import logging
from flask_restful_swagger_2 import Resource, swagger
from datetime import datetime
from net.route.SwaggerSchema import *


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

        temestamp = datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
        PEOPLE = {
            "Farrell": {
                "fname": "Doug",
                "lname": "Farrell",
                "timestamp": temestamp
            },
            "Brockman": {
                "fname": "Kent",
                "lname": "Brockman",
                "timestamp": temestamp
            },
            "Easter": {
                "fname": "Bunny",
                "lname": "Easter",
                "timestamp": temestamp
            }
        }
        return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

