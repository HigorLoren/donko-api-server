import json
from flask import Blueprint, jsonify, request

# define the blueprint
blueprint_user = Blueprint(name="blueprint_user", import_name=__name__)


@blueprint_user.route('/authenticate', methods=['POST'])
def authenticate():
    request_data = request.get_json()

    output = {}

    if request_data:
        if (request_data['emailAddress'] == 'test@example.com'):
            from faker import Faker
            fake = Faker()
            output['token'] = fake.bothify(text='########')
            output['user'] = {}
            output['user']['name'] = fake.user_name()
            output['user']['image'] = 'https://api.lorem.space/image/face?w=150&h=150'

    return jsonify(output)


@blueprint_user.route('/', methods=['GET'])
def get():
    data = request.get_json()
    token = request.args.get('token', '')

    if (token):
        output = {}
        from faker import Faker
        fake = Faker()
        output['name'] = fake.user_name()
        output['image'] = 'https://api.lorem.space/image/face?w=150&h=150'

        return jsonify(output)

    return {}, 401