__author__ = 'ManiKanta Kandagatla'

from Parent import Parent

class Child(Parent):

    def __init__(self):
        print 'Constructor called'
        Parent.__init__(self,1,2,3,4,5)

def main():
    child = Child()
    print child.getValue1()
    print child.class_variable

    Child.class_variable = 10
    child2 = Child()
    print child2.class_variable
main()