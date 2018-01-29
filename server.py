#!/usr/bin/python
# -*- coding: UTF-8 -*-


from wsgiref.simple_server import make_server



from hello import application


httpd = make_server('', 8086, application)

print("Serving HTTP on port 8086...")


httpd.serve_forever()

test1