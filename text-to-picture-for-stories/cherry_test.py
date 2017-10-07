import os, os.path
import random
import string
import html_parse as pr
import cherrypy
cherrypy.config.update({'server.socket_port': 8008})
cherrypy.engine.restart()

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')
        
    @cherrypy.expose
    def gen(self,title,story):
        s=open('generate.html','r').read()
        s=s.replace('{{title}}',title)
        st=story.split('.')
        body=[]
        for i in st:
            body.append(pr.get_cont(i,title))
        rep='\n'.join(body)
        s=s.replace('{{body}}',rep)
        return s
        

        



        

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'engine.autoreload_on': False,
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    
    webapp = StringGenerator()
    #webapp.generator = StringGeneratorWebService()
    cherrypy.quickstart(webapp, '/', conf)