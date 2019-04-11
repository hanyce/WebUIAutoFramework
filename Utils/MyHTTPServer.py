#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# !coding=UTF-8
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import socketserver
import sys


method_api = {
    "login": lambda **kwargs: "login {}".format(kwargs)
}


class MyThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    pass


class MyHttpHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        encode_type = "utf-8"
        if self.path.startswith("/api/?"):
            raw_string = self.path.replace("/api/?", "")
            query_string = urllib.parse.unquote(raw_string)
            _params = urllib.parse.parse_qs(query_string)
            params = {k: v[0] for k, v in _params.items()}
            if "method" not in params:
                message = "失败: 没有填写method参数"
            else:
                method = params["method"]
                if method not in method_api:
                    message = "失败: method参数值不存在"
                else:
                    params.pop("method")
                    try:
                        result = method_api[method](**params)
                        message = "调用成功: {0}".format(result)
                    except Exception:
                        exc_type, exc_msg, _ = sys.exc_info()
                        message = "调用失败, {0}: {1}".format(exc_type.__name__, exc_msg)
            message = message.encode(encode_type)
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset={0}".format(encode_type))
            self.end_headers()
            self.request.send(message)
        else:
            self.send_error(404)


if __name__ == '__main__':
    httpd = MyThreadingHTTPServer(('', 8080), MyHttpHandler)
    print("Server started on 127.0.0.1, port 8080.....")
    httpd.serve_forever()
