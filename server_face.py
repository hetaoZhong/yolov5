from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from cgi import parse_header, parse_multipart
import cgi
import urllib.parse as parse
import json
import detect_face


data = {'result': 'this is a test'}
host = ('192.168.25.92', 7002)


class Resquest(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header('Content-Type', 'application/json;charset=UTF-8')
        self.end_headers()
        parsed_path = parse.urlparse(self.path)
        arr_str = self.path.split('/')
        print(self.path)
        # save received images to the path ./images/filename
        if arr_str[1] == 'detect':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         }
            )
            zoom = form.getvalue('zoom')
            is_blur = form.getvalue('isBlur')
            byte_file = form.getvalue('file')
            # print(type(byte_file))
            detect_face.main()
            self.wfile.write(json.dumps(text_list, ensure_ascii=False).encode())


if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
