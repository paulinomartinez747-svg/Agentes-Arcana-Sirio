#!/usr/bin/env python3
import http.server, json, urllib.request

DEEPSEEK = "https://api.deepseek.com/v1"
KEY = "sk-5402bd3954494db88904766a3ff923c7"

class Proxy(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self._proxy("GET")
    def do_POST(self):
        self._proxy("POST")
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()
    
    def _proxy(self, method):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length else None
        path = self.path
        if path.startswith('/v1/'):
            path = path[3:]  # strip /v1 to avoid doubling
        url = DEEPSEEK + path
        req = urllib.request.Request(url, data=body, method=method)
        req.add_header('Authorization', 'Bearer ' + KEY)
        req.add_header('Content-Type', 'application/json')
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = resp.read()
                self.send_response(resp.status)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(data)
        except Exception as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    def log_message(self, format, *args):
        pass

http.server.HTTPServer(('0.0.0.0', 4000), Proxy).serve_forever()

