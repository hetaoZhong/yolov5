from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import detect_face
import detect_robber_npc
import time
import random
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import cgi
import urllib.parse as parse
import uuid
from PIL import Image
from io import BytesIO

data = {'result': 'this is a test'}
host = ('localhost', 8888)


def save_file(self):
    form = cgi.FieldStorage(
        fp=self.rfile,
        headers=self.headers,
        environ={'REQUEST_METHOD': 'POST',
                 'CONTENT_TYPE': self.headers['Content-Type'],
                 }
    )
    byte_file = form.getvalue('file')
    # 存储文件
    uname = uuid.uuid1().hex
    uname = uname + '.png'
    image = Image.open(BytesIO(byte_file))
    image.save('E:/YOLO_TEMP_FILE/'+uname)
    return uname


class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        t1 = time.time()
        url = self.path
        result = ''
        if url == '/detect':
            detect_face.detect_result = ''
            detect_face.check_requirements(exclude=('tensorboard', 'thop'))
            opt = detect_face.parse_opt()
            detect_face.run(**vars(opt))
            result = detect_face.detect_result
        elif url == '/detect_robber_npc':
            detect_robber_npc.detect_result = ''
            detect_robber_npc.check_requirements(exclude=('tensorboard', 'thop'))
            opt = detect_robber_npc.parse_opt()
            detect_robber_npc.run(**vars(opt))
            result = detect_robber_npc.detect_result
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())
        t2 = time.time()
        print("cost::"+str(t2-t1))

    def do_POST(self):
        t1 = time.time()
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header('Content-Type', 'application/json;charset=UTF-8')
        self.end_headers()
        parsed_path = parse.urlparse(self.path)
        arr_str = self.path.split('/')
        print(self.path)

        # 检测打宝图相关的NPC
        if arr_str[1] == 'detect_face':
            uname = save_file(self)
            detect_face.detect_result = ''
            detect_face.check_requirements(exclude=('tensorboard', 'thop'))
            opt = detect_face.parse_opt(uname)
            detect_face.run(**vars(opt))
            result = detect_face.detect_result
            print('result::'+result)
            self.wfile.write(json.dumps(result, ensure_ascii=False).encode())
        elif arr_str[1] == 'detect_robber_npc':
            # 获取文件
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         }
            )
            byte_file = form.getvalue('file')
            # 存储文件
            uname = uuid.uuid1().hex
            uname = uname+'.png'
            with open('files/'+uname+'.png', 'wb+') as desctination:
                for chunk in byte_file.chunks:
                    desctination.write(chunk)
            # 开始检测
            detect_robber_npc.detect_result = ''
            detect_robber_npc.check_requirements(exclude=('tensorboard', 'thop'))
            opt = detect_robber_npc.parse_opt(uname)
            detect_robber_npc.run(**vars(opt))
            result = detect_robber_npc.detect_result
            print(result)
            self.wfile.write(json.dumps(result, ensure_ascii=False).encode())

        t2 = time.time()
        print(str(t2-t1))




if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
