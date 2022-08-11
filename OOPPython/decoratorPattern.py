from functools import wraps

def make_blink(function):
    ''' Defines the decorator '''

    @wraps(function)

    def decorator():
        ret = function()

        return "<blink>" + ret + "</blink>"

    return decorator

@make_blink
def hello_world():
    ''' Original function '''
    return "Hello world!"

print(hello_world())
print(hello_world.__name__)
print(hello_world.__doc__)
