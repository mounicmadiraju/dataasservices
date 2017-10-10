__author__ = 'sahara'

import os
import unittest
import threading
from flask import Flask, Blueprint, request
from flask_deploy import get_server
import requests
import time

def _start_server(server):
    print "Starting server"
    try:
        server.start()
    finally:
        server.stop()


class BaseTestCase(unittest.TestCase):
    server_name = None
    server = None
    thread = None
    address = "localhost:8000"

    def __init__(self, *args, **kwargs):
        super(BaseTestCase, self).__init__(*args, **kwargs)
        self.enabled = False

    def _start_server(self):
        self.server.start()

    @classmethod
    def setUpClass(cls):
        if cls.server_name is not None:
            app = Flask(__name__)
            bp = Blueprint("bp", __name__)

            @app.route('/', methods=["GET","POST"])
            def index():
                if request.method=="GET":
                    return "Hello World!"
                else:
                    value = request.data
                    print value
                    return "Hello "+value+" World!"

            @bp.route("/test/",methods=["GET"])
            def blueprint_route():
                return "Hello Testy World!"

            app.register_blueprint(bp, url_prefix="/app")

            Server = get_server(cls.server_name)
            cls.server = Server(app)
            cls.thread = threading.Thread(target=_start_server, args=(cls.server,))
            cls.thread.daemon = True
            cls.thread.start()
        else:
            pass

    @classmethod
    def tearDownClass(cls):
        if cls.server_name is not None:
            if cls.thread.isAlive():
                cls.thread._Thread__stop()


class TestWerkzeugServer(BaseTestCase):
    server_name = "Werkzeug"

    def test_fetch_index(self):
        res = requests.get("http://localhost:8000/")
        print res.text
        assert res.text == 'Hello World!'

    def test_put_index(self):
        data = "Special"
        res = requests.post("http://localhost:8000/",data=data)
        print res.text
        assert res.text == "Hello "+data+" World!"

    def test_fetch_blueprint(self):
        res = requests.get("http://localhost:8000/app/test/")
        print res.text
        assert res.text == 'Hello Testy World!'

    def test_server_name(self):
        res = requests.get("http://localhost:8000/")
        try:
            server_headers = res.headers['server']
            server = server_headers.split('/')[0]
            print "Servernmae ",server
            assert server == self.server_name
        except KeyError:
            print "Server name not found"
            assert 1==0

#class TestFapws3Server(BaseTestCase):
#    server_name = "fapws3"

class GeventServer(BaseTestCase):
    server_name = "Gevent"

    def test_fetch_index(self):
        res = requests.get("http://localhost:8000/")
        print res.text
        assert res.text == 'Hello World!'

    def test_put_index(self):
        data = "Special"
        res = requests.post("http://localhost:8000/",data=data)
        print res.text
        assert res.text == "Hello "+data+" World!"

    def test_fetch_blueprint(self):
        res = requests.get("http://localhost:8000/app/test/")
        print res.text
        assert res.text == 'Hello Testy World!'

    def test_server_name(self):
        res = requests.get("http://localhost:8000/")
        try:
            server_headers = res.headers['server']
            server = server_headers.split('/')[0]
            print "Servernmae ",server
            assert server == self.server_name
        except KeyError:
            print "Server name not found"
            assert 1==0
