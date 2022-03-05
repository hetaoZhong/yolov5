from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import detect_face

data = {'result': 'this is a test'}
host = ('localhost', 8888)


class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path
        if url == '/detect':
            detect_face.detect_result = ''
            detect_face.check_requirements(exclude=('tensorboard', 'thop'))
            opt = detect_face.parse_opt()
            detect_face.run(**vars(opt))
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(detect_face.detect_result).encode())


if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
