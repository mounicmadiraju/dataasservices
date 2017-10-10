__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__author__ = 'Sahara Raju'
__license__ = 'MIT'
__copyright__ = '(c) 2017 by Sahara Raju'
__all__ = ['FlaskDebugServer']


class WebServer(object):
    def __init__(self,app,host,port, base_url, debug, reloader):
        self.app = app
        self.host = host
        self.port = port
        self.base_url = base_url
        self.debug = debug
        self.reloader = reloader
        self.server = None
        
        
class GeventServer(WebServer):

    def __init__(self,app, host='0.0.0.0', port=8000,base_url='/', debug=False, reloader=False):
        super(self.__class__,self).__init__(app,host,port,base_url,debug,reloader)

    def start(self):
        from gevent import wsgi
        self.server = wsgi.WSGIServer(('', self.port), self.app)
        gevent.signal(signal.SIGTERM, self._shutdown)
        self.server.serve_forever()

    def stop(self):
        self.server.stop()

    def _shutdown():
      print('Shutting down ...')
      server.stop(timeout=60)
      exit(signal.SIGTERM)



class WerkzeugServer(WebServer):
    def __init__(self, app, host='0.0.0.0', port=8000,base_url='/', debug=False, reloader=False):
        super(self.__class__,self).__init__(app,host,port,base_url,debug,reloader)

    def start(self):
        self.app.run(self.host, self.port, self.debug)

    def stop(self):
        pass


class Fapws3Server(WebServer):
    def __init__(self, app,host='0.0.0.0', port=8000,base_url='/', debug=False, reloader=False):
        super(self.__class__,self).__init__(app,host,port,base_url,debug,reloader)

    def start(self):

        import fapws._evwsgi as evwsgi
        from fapws import base

        self.server = evwsgi
        self.server.start(self.host,str(self.port))
        self.server.set_base_module(base)
        self.server.wsgi_cb((self.base_url,self.app))
        self.server.set_debug(self.debug)
        self.server.run()

    def stop(self):
        pass


_servers = {'Werkzeug': WerkzeugServer,
            'fapws3': Fapws3Server,
            'Gevent': GeventServer}


def get_server(server_name):
    global _servers

    try:
        return _servers[server_name]
    except KeyError:
        raise NotImplementedError("Unknown or incorrect server name, %s"%server_name)

if __name__ == '__main__':
    from flask import Flask, request
    app = Flask(__name__)

    @app.route('/', methods=["GET","POST"])
    def index():
        if request.method=="GET":
            return "Hello World!"
        else:
            value = request.data
            print value
            return "Hello "+value+" World!"

    Server = get_server("Werkzeug")
    server = Server(app)
    server.start()