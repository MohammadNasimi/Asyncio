import grpc
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
from time import sleep,perf_counter

class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))
        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        start = perf_counter()
        message = pb2.Message(message=message)
        print(f'{message}')
        a = self.stub.GetServerResponse(message)
        end = perf_counter()
        T = end - start
        return T,a


if __name__ == '__main__':
    client = UnaryClient()
    result = client.get_url(message="Hello Server you there?")
    print(f'{result}')