import time

class Producer:
    ''' Defines the resource intensive object to instantiate '''

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:
    ''' Less resource intensive class to instantiate to check if the produce is available '''
    def __init__(self):
        self.occuppied = "No"
        self.producer = None

    def produce(self):
        ''' Check if producer is available '''
        print("Artist is checking if producer is available . . .")
        
        if self.occuppied == "No":
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()

        else:
            time.sleep(2)
            print("Producer is working hard")
    
proxy = Proxy()
proxy.produce()
proxy.occuppied = "Yes"
proxy.produce()

