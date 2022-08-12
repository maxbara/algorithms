
class Subject: 
    '''Represents what is being observed'''

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        # attaches observer to the list, if that observer is not present already
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        ''' Notifies each observer by calling their update() method'''
        for o in self._observers:
            if o != modifier:
                o.update(self)

class Core(Subject):
    '''Inherits from subject class plus adds properties'''

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        '''Implements a setter that notifies observers'''
        self._temp = temp
        self.notify()

class TempViewer:
    '''Views the temperature changes for a subject '''
    def update(self, subject):
        print('Temperature Viewer: {} has Temperature {}'.format(subject._name, subject.temp))

    def update_temp(self, subject, temp):
        '''Updates the temp itself, so this observer will not be notified like the other observers will'''
        subject._temp = 999
        subject.notify(self)


city1 = Core("Tegucigalpa")
city2 = Core("Seattle")  

v1 = TempViewer()
v2 = TempViewer()
v3 = TempViewer()

city1.attach(v1)
city1.attach(v3)
city2.attach(v2)

city1.temp = 80
city2.temp = 100

v1.update_temp(city1, 999)






