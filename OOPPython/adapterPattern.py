
class Korean:
    ''' Korean Speaker '''
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"

class French:
    ''' French Speaker '''
    def __init__(self):
        self.name = "French"

    def speak_french(self):
        return "Bonjour!"

class Adapter:
    ''' Adapts different methods to be called from 1 common method '''
    def __init__(self, obj, **methodkv):
        self._object = obj
        self.__dict__.update(methodkv)
    
    def __getattr__(self, attr):
        return getattr(self._object, attr)

korean = Korean()
french = French()
objs = []
objs.append(Adapter(korean, speak = korean.speak_korean))
objs.append(Adapter(french, speak = french.speak_french))

for obj in objs:
    print('{} says {}'.format(obj.name, obj.speak()))