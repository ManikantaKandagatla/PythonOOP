__author__ = 'ManiKanta Kandagatla'


class Parent(object):
    class_variable = 1
    def __init__(self, value1, value2, public_value, protected_value, private_value):
        self.value1 = value1
        self.value2 = value2
        self.public_value = public_value
        self._protected_value = protected_value
        self.__private_value = private_value
        self.class_variable = self.class_variable + 1


    def getValue1(self):
        return self.value1
    def getValue2(self):
        return self.value2
    def get_public_value(self):
        return self.public_value
    def get_private_value(self):
        return self.__private_value
    def get_protected_value(self):
        return  self._protected_value