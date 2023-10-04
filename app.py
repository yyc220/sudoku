
import copy
import threading
import json

from flask import Flask, render_template, request,redirect,url_for,make_response,jsonify
from generate import generateBoards, removeNumbers
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/start_game', methods=['POST'])
def start_app():
    diff = request.get_data()
    return redirect(url_for('index', difficulty=diff))


@app.route('/sudoku_data')
def index():
    diff = request.args.get('difficulty')
    count = 0
    if diff == 'easy':
        count = 30
    elif diff == 'medium':
        count = 40
    else:
        count = 50

    # 创建一个空列表用于保存生成的九个数独谜题
    sudokus = []

    # 定义生成数独的函数
    def generate_sudoku():
        sudoku = generateBoards()
        dighole = copy.deepcopy(sudoku)
        removeNumbers(dighole, count)
        return (sudoku, dighole)

    # 创建九个线程，每个线程生成一个数独谜题并将其保存到列表中
    threads = []
    for _ in range(9):
        thread = threading.Thread(target=lambda: sudokus.append(generate_sudoku()))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成生成任务
    for thread in threads:
        thread.join()

    # 将九个数独谜题传递给模板进行渲染
    sudos = json.dumps(sudokus)
    rt = render_template('sudoku_9.html', sudos=sudos)
    rt = jsonify(sudos=sudokus)
    print(rt)
    return(rt)
    # response = make_response(rt)
    # response.headers['Content-Type'] = 'text/html'
    # return response




if __name__ == '__main__':
    app.run()