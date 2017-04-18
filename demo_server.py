# -*- coding: utf-8 -*-

# Server API demo
#
# 启动：python3 demo_server.py
#
# Author: Alex
# Created Time: 2017年04月18日 星期二 17时09分32秒

from jpype import *
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_restful.representations.json import output_json

hanLPLibPath = '/var/hanlp/hanlp-1.3.2-release/'
javaClassPath = hanLPLibPath+'hanlp-1.3.2.jar'+':'+hanLPLibPath

startJVM(getDefaultJVMPath(), '-Djava.class.path='+javaClassPath, '-Xms1g', '-Xmx1g')
HanLP = JClass('com.hankcs.hanlp.HanLP')


# 服务器初始化
#output_json.func_globals['settings'] = {
    #'ensure_ascii': False,
    #'encoding': 'utf8',
#}

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('content', type=str, help='输入的文本')


#@api.representation('application/json; charset=utf-8')


def succ(data):
    return {"code": 0, "data": data}


class segment(Resource):
    def post(self):
        parser.add_argument('method', type=str, required=False)
        method = parser.parse_args()['method']
        content = parser.parse_args()['content']
        print(content)

        if method == "stardard":
            return self._stardard(content)

    def _stardard(self, content):
        segments = []
        termList = HanLP.segment(content)
        for i in range(len(termList)):
            term = termList[i]
            segments.append(str(term))
        return succ(segments)



api.add_resource(segment, '/segment')

if __name__ == '__main__':
    app.run('0.0.0.0', 5001, debug=False)
