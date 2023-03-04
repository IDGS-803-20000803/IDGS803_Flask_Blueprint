from flask import Blueprint
directivos = Blueprint('dir', __name__)

@directivos.route('/getdir', methods=['GET'])
def getdir():
    return {'key' : 'Directivos'}