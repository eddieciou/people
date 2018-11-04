from flask_restful_swagger_2 import Resource, swagger
from datetime import datetime

class GetPelple(Resource):
    @swagger.doc({
        'tags': ['PeopleAPI'],
        'description' : '取得人員清單',
        'responses' :{
            '200' : {
                'description' : '顯示人員清單',
                'schema' : {
                    'type' : 'array',
                    'items' : {
                        'properties' : {
                            'fname' : {
                                'type' : 'string'
                            },
                            'lname': {
                                'type': 'string'
                            },
                            'timestamp': {
                                'type': 'string'
                            }
                        }
                    }
                }
            }
        }
    })
    def get(self):
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

