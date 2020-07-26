# -*- coding: utf-8 -*-


def test_thrift_client():
    from folklore import Folklore
    from folklore.testing import ThriftClient

    app = Folklore('TestService')

    @app.api
    def say_hello(name):
        return 'Hello ' + name

    c = ThriftClient(app)
    assert c.say_hello('world').value == 'Hello world'
