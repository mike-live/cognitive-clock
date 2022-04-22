import pandas as pd
from cognitive_clock import cognitive_clock

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
from io import StringIO
import json

class server(BaseHTTPRequestHandler):
    calculator = cognitive_clock()

    def process_request(self, request):
        response = ''
        try:
            tests_258 = pd.read_csv(StringIO(request['T258']), sep=';')
            tests_274 = pd.read_csv(StringIO(request['T274']), sep=';')
            tests_278 = pd.read_csv(StringIO(request['T278']), sep=';')
            cognitive_clock = self.calculator.compute_cognitive_age(tests_258, tests_274, tests_278)

            response = {
                'status': 'ok',
                'cognitive_clock': cognitive_clock
            }
        except Exception as err:
            print('Error', err)
            response = {
                'status': 'error'
            }
        return response

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        request = json.loads(body)
        result = json.dumps(self.process_request(request))
        print(result)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = BytesIO()
        response.write(result.encode())
        self.wfile.write(response.getvalue())


from http.server import HTTPServer, BaseHTTPRequestHandler

httpd = HTTPServer(('localhost', 8585), server)
httpd.serve_forever()