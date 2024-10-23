class person( object ):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee( person ):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post  = post
        person.__init__(self, name, idnumber)
    def display1(self):
        print(self.salary)
        print(self.post)
a = employee("Mustafa", 88007766, 500000, "CEO")
a.display()
a.display1()