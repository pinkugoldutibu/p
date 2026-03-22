class Myclass():
    __privateVar = 27 ;
    def __privMeth(self):
        print("I'am inside class ")
    def hello():
        print("pivate Varible value: ", Myclass.__privateVar)
foo = Myclass()
foo.hello()
foo.__privMeth