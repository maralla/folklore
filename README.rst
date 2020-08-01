Folklore: Elegant thrift service development framework
======================================================

.. image:: https://travis-ci.org/maralla/folklore.svg?branch=master
    :target: https://travis-ci.org/maralla/folklore



This package defines the interfaces for writing Folklore thrift services.

Install
-------

.. code:: bash

    pip install folklore


Example
-------

To define an app:

.. code:: python

    # app.py
    from folklore import Folklore

    app = Folklore('TestService')

    @app.api
    def say_hello(name):
        return 'Hello ' + name


To Run the app, install `folklore-cli <https://github.com/maralla/folklore-cli>`_ first, then
create the following config:

.. code:: thrift

    # ping.thrift
    service TestService {
        string say_hello(1: required string name)
    }

.. code:: yaml

    # app.yaml
    app_name: test_app
    app: app:app
    thrift_file: ping.thrift

Run the following command:

.. code:: bash

    $ folklore serve
