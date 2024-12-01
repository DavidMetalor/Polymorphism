class eagle: 
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name)
        print(self.age)
    def make_sound(self):
        print("whistle")

class hawk:
   def __init__(self, name, age):
        self.name=name
        self.age=age
   def info(self):
        print(self.name)
        print(self.age)
   def make_sound(self): 
       print("call")

obj1=eagle("task",2)
obj2=hawk("kit",1)
for i in(obj1, obj2): 
    i.info()
    i.make_sound()
    