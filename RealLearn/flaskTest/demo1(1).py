from flask import Flask, jsonify, request, make_response

# app = Flask(__name__)
# @app.route('/', methods=['GET'])
# def index():
#     return 'hello'
#
# if __name__ == '__main__':
#     app.run()


app = Flask(__name__)
# print(app)
path = '/api/v1.0'
tasks = [
    {'id':1,
     'data':'哈哈'
     },
    {'id':2,
     'data':'呵呵'}
         ]


# @app.route(path + '/tasks',methods=['GET'])
# def getTasks():
#     return jsonify({"tasks":tasks})

# @app.route(path + '/tasks/<int:id>', methods = ['GET'])
# def getTaskById(id):
#     for x in tasks:
#         if x['id'] == id:
#             return jsonify({'tasks':x})
#     return ({'error': 'Not found'})

# @app.route(path + '/tasks', methods = ['POST'])
# def createTask():
#     # print (request.headers)
#     # if not request.json or 'data' not in request:  # 不知道什么意思
#     #     print('aaa',request.json)
#     #     return "Resquest Data Error"
#     task = {'id':tasks[-1]['id'] +1,
#             'data':request.json['data'],}
#     tasks.append(task)
#     return jsonify({'task': task}), 201

# path = '/api/v1.0/tasks/<int:id>'
# @app.route(path + '/tasks/<int:id>', methods=['PUT'])
# def updataTask(id):
#     for x in tasks:
#         if id == x['id']:
#             x['data'] = '我啊'
#             return jsonify({"tasks":tasks})

# http://127.0.0.1:5000/api/v1.0/tasks/[task_id]
import json
@app.route(path + '/tasks/<int:id>', methods=['DELETE']) # @app.route()是thedecorator是装饰index()功能
def deleteTask(id):
    print(request.headers)
    for x in tasks:
        if id == x['id']:
             tasks.remove(x)
             # return json.dumps({'tasks':tasks})
             return jsonify({'tasks':tasks})
    return not_found("id %s not found:"%(str(id)))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(error), 404)

@app.errorhandler(400)
def error_request(error):
    return make_response(jsonify(error),400)




if __name__ == '__main__':
    app.debug = True
    app.run()

# import json
# import requests
# url = 'http://t-ifwzx.hfjy.com/contract/pay'
# head = {'Authorization':'Bearer da89d451-2224-4015-ae0c-a10fccd482591547106821834'}
# data = {'contractId': 'X20011901000054',
#         'payMethodNew': "yinlian",
#         'payParam': {},
#         'payType': "2",
#         'sum': 0.01,
#         'installment': 3}
# r = requests.request('post',url, params=data, headers=head)
# print(r.json())


