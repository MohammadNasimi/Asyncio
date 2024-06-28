import grpc
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
from time import sleep
import pika
class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='grpc_queue')

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'hi your messsage"{message}" message from you'
        result = {'message': result, 'received': True}
        sleep(30)
        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()