# -*- coding:utf-8 -*-

from flask import Flask, jsonify, abort, request

app = Flask(__name__)

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


@app.route("/")
def home():
    return "hello world"


# 获取所有task信息
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
# 测试命令：curl -i http://localhost:5000/todo/api/v1.0/tasks/2


# 根据id获取task信息
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# 测试命令：curl -i http://localhost:5000/todo/api/v1.0/tasks/2


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    # if not request.json or not 'title' in request.json:
    #     abort(400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'tasks': tasks}),201
    # 测试命令：curl -i -H "Content-Type:application/json" -X POST -d '{"title":"Read a book"}' http:
    # //localhost:5000/todo/api/v1.0/tasks


if __name__ == "__main__":
    app.run(debug=True)