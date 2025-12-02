from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/welcome":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        try:
            data = json.loads(body)
            name = data.get("name")
            if not name:
                raise ValueError
        except:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")
            return

        message = {
            "message": f"Hello {name}, welcome to Wellspring University Distributed Systems Server by Omoregbee Aisosa."
        }

        resp = json.dumps(message).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(resp)))
        self.end_headers()
        self.wfile.write(resp)

def run():
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("running on port 8000")
    server.serve_forever()
    

if __name__ == "__main__":
    run()
