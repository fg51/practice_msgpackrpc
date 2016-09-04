"""
<a href="http://qiita.com/ikuyamada/items/a75088fe5728273c2e41">Pythonで高速なRPCを実装する - Qiita</a>
"""

import msgpackrpc

class FooServer:
    def func(self, x, y):
        return x + y

def main():
    server = msgpackrpc.Server(FooServer())
    server.listen(msgpackrpc.Address("localhost", 3000))
    server.start()


#from gevent.server import StreamServer
#from mprpc import RPCServer
#
#class FooServer(RPCServer):
#    def func(self, x, y):
#        return x + y
#
#def main():
#    server = StreamServer(("localhost", 3000), FooServer())
#    server.serve_forever()


if __name__ == '__main__':
    main()
