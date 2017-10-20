class Test(object):
    def __init__(self,name):
        self.name = name
    @property
    def test1(self):
        return self.name

    @test1.setter
    def test2(self,name):
        self.name = name
    
test = Test('123')
print(test.test1)
test.test2 = '456'
print(test.test1)