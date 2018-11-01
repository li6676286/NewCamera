import threading

import bottle
class HttpServer:
    def _run(self, cb):
        @bottle.post('/hxzx')
        def post():
            cb(bottle.request.body.read().decode())
            # self._http_callback(bottle.request.body.read().decode())
        bottle.run(host='0.0.0.0', port=8000)

    def run_daemon(self, cb):
        t = threading.Thread(target=self._run, args=(cb,))
        t.daemon = True
        t.start()