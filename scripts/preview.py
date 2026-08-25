#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
PORT = int(os.environ.get('PORT', '8080'))
HOST = os.environ.get('HOST', '127.0.0.1')

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_GET(self):
        path = self.path.split('?', 1)[0]
        if path == '/healthz':
            body = b'ok\n'
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if path == '/api/health':
            body = b'{"ok":true,"service":"malach-application","status":"operational"}'
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        candidate = ROOT / path.lstrip('/')
        if path == '/':
            candidate = ROOT / 'index.html'
        elif candidate.is_dir():
            candidate = candidate / 'index.html'
        elif not candidate.suffix:
            candidate = candidate / 'index.html'
        self.path = '/' + (candidate.relative_to(ROOT).as_posix() if candidate.exists() and candidate.is_file() else '404.html')
        super().do_GET()

if __name__ == '__main__':
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    display_host = '127.0.0.1' if HOST in ('0.0.0.0','::') else HOST
    print(f'Malach preview: http://{display_host}:{PORT}', flush=True)
    if HOST == '0.0.0.0':
        print('LAN preview enabled: open http://<your-mac-ip>:%s on your phone' % PORT, flush=True)
    server.serve_forever()
