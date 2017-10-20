a=1

class test(object):
    def __init__(self):
        self.name = a 
    @property
    def call_name(self):
        return self.name

print(test().call_name)