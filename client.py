import sys
sys.path.append('./gen-py')

from tutorial import Calculator;
from tutorial.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
	transport = TSocket.TSocket('localhost', 9090);

	transport = TTransport.TBufferedTransport(transport);

	protocol = TBinaryProtocol.TBinaryProtocol(transport);

	# Create A client
	client = Calculator.Client(protocol)

	# connect
	transport.open()

	client.ping()

main()