from flask_restful_swagger_2 import Schema

class PeopleList_RModel(Schema):
    type = 'object'
    properties = {
        'fname'    : {'type': 'string', 'description':'firstname'},
        'lname'    : {'type': 'string', 'description':'lastname'},
        'timestamp': {'type': 'string', 'description':'timestamp'}
    }