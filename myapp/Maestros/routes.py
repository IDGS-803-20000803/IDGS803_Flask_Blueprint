from flask import Blueprint
maestros = Blueprint('maestros', __name__)

@dir.route('/getmaes', methods=['GET'])
def getmaes():
    return {'key' : 'Maestros'}