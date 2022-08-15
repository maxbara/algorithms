
class Component:
    '''Abstract Class'''

    def __init__(self, *args, **kwargs):
        pass
    
    def component_function(self):
        pass

class Child(Component): # inherits from the abstract class Component
    '''Concrete Class'''

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # Store name of child class
        self.name = args[0]

    def component_function(self):
        # Print the name of your child item here!
        print("{}".format(self.name))

class Composite(Component):
    '''Concrete class and maintains the tree recurisve structure'''

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # stores the name of the composite obj
        self.name = args[0]

        # list of children
        self.children = []

    def append_child(self, child):
        '''Method to add new child item'''
        self.children.append(child)

    def remove_child(self, child):
        '''Method to remove child item'''
        self.children.remove(child)

    def component_function(self):

        #Print the name of the composite object
        print("{}".format(self.name))

        # invoke children objects' component_function
        for i in self.children:
            i.component_function()

# build menu
top = Composite("top_menu")
submenu1 = Composite("submenu1")
submenu1.append_child(Child("sub_submenu11"))
submenu1.append_child(Child("sub_submenu12"))
submenu2 = Composite("submenu2")
top.append_child(submenu1)
top.append_child(submenu2)

top.component_function()

print()

top.remove_child(submenu1)

top.component_function()
