import types

class Strategy:
    '''Strategy pattern'''

    def __init__(self, function=None):
        self._name = "Default strategy"
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print("Executing: {}".format(self._name))

def strategy_one(self):
    print("Executing strategy 1")


def strategy_two(self):
    print("Executing strategy 2")

s = Strategy()
s.execute()

s = Strategy(strategy_one)
s.execute()

s = Strategy(strategy_two)
s.execute()