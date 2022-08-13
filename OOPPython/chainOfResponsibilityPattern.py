

class Handler:
    '''Abstract Handler to be used for concrete handlers'''

    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("This handler is not implemented")

class FirstConcreteHandler(Handler):
    '''First concrete handler'''

    def _handle(self, request):
        if 0 < request < 10:
            print('Request: {} handled by: {}'.format(request, self.__class__.__name__))
            return True

        return False

class DefaultHandler(Handler):
    '''Default Handler to stop the handling delegation'''

    def _handle(self, request):
        print('End of chain. No handler for request: {}'.format(request))
        return True

class Client:
    '''Client that actually delegates by using the handlers'''  

    def __init__(self, handler):
        self._handler = handler

    def delegate(self, requests):
        '''Delegates the work through the chain of responsibility'''
        for r in requests:
            self._handler.handle(r)


client = Client(FirstConcreteHandler(DefaultHandler(None)))

requests = [2, 30, 4]

client.delegate(requests)
