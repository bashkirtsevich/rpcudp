from rpcudp.protocol import RPCProtocol
from twisted.python import log
from twisted.internet import reactor
import sys

log.startLogging(sys.stdout)

class RPCServer(RPCProtocol):
    def rpc_sayhi(self, name):
        # This could return a Deferred as well
        return "Hello %s" % name

server = RPCServer(1234)

class RPCClient(RPCProtocol):
    def handleResult(self, result):
        if result[0]:
            print "Success! %s" % result[1]
        else:
            print "Response not received."

client = RPCClient(5678)
client.sayhi(('127.0.0.1', 1234), "Snake Plissken").addCallback(client.handleResult)

reactor.run()
