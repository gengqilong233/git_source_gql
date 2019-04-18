from flask import Flask, request, make_response, redirect, abort, render_template, url_for
from flask_bootstrap import Bootstrap
import time

app = Flask(__name__) # Flask的构造函数必须有一个指定参数，一般为Python的__nam__或者包名
# 将__name__传给Flask，因为：这个参数决定了程序的根目录，可以找到此程序的相对根目录及 资源文件位置
print('name:%s' %app)

@app.route('/') # 装饰器route用于映射访问路由
def index():
    user_agent = request.headers.get('user_Agent') # 通过这句可获得头信息
    # return '<h1>hello<h1>' # 简单的页面返回hello
    # return '<p>另一个是%s<p>' %user_agent, 400 # 设置状态码

    # print(request.headers)
    # response = make_response('<h1>this document carries a cookie!</h1>')
    # response.set_cookie('answer', '42') # 设置cookie信息
    # return response

    # return redirect('http://i.hfjy.com/resource/index.html#!/') # 重定向 redirect()

    return render_template('index.html')

data = [
    {'id':'1',
     'user':'用户1'},
    {'id':'2',
     'user':'用户2'}
]

@app.route('/id/<id>') # <> 内的内容就是动态部分，任何能匹配静态部分的URL都会映射到这个路由上
def id(id):
    for x in data:
        if x['id'] == id:
            # return '<h1>hello %s<h1>' % x['user']
            return render_template('user.html', user=x['user'])
        else:
            abort(404) # 动态参数如不存在，返回404或设置的值


@app.route('/user/<user>')
def user(user):
    for x in data:
        if x['user'] == user: # 参数在data中时可以用user.html中if判断和for循环
            return render_template('user.html', user=x),404 # 这样给代码设置404响应的话是不会返回404页面的，需要用到id函数的 abort(404)
        else:
            return  render_template('user.html', user='') # 不在的话只能用for循环


@app.errorhandler(404)
def not_found_page(e):
    return render_template('404.html'),404

with app.test_request_context(): # url_for操作的对象是函数，而不是route里的路径
    print('index:',url_for('index', _external=True)) # 返回绝对路径，可以用_external=True参数,但是并没有卵用，没有显示端口号，跟下边一样拼一个处理吧
    print('id:', 'http://localhost:5000'+url_for('id', id=1)) # 路由有动态参数的话就跟这两行一样传
    print('user:', 'http://localhost:5000'+url_for('user',user='lala'))

if __name__ == '__main__':
    app.debug = True # 调试模式
    app.run(port=5000) # run方法启动服务
    # app.run(debug=True) 上两行简写

