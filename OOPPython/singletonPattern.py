

class Borg:

    _shared_data = dict()

    def __init__(self):

        self._shared_data = self._shared_data


class ExampleSingleton(Borg):

    def __init__(self, **kwargs):

        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)


x = ExampleSingleton(http = "http details")

y = ExampleSingleton(tcp = "tcp details")

print(x)
print(y)


print()
print("_________")
print("The other ways to create a singleton class are several, yet have their drawback and aren't straight forward. I prefer the borg pattern")
