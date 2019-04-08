#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask import abort

app = Flask(__name__)

items = [
    {
        "id": "1",
        "address": "house1",
        "insured_total": 1000,
    },
    {
        "id": "2",
        "address": "house2",
        "insured_total": 10000,
    }
]

#
# @app.route('/iroha_rest/api/v1.0/items', methods=['POST'])
# def put_item():
#     item = {
#         "id": tasks[-1]['id'] + 1,
#         "address": request.json["address"],
#         "insured_total": request.json["insured_total"]
#     }
#     items.append(item)
#     return jsonify({'item': item}), 201


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)


# Result:
