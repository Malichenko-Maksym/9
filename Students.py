class Student():
    ID=100000
    def __init__(self,name,surname,field):
        self.name=name
        self.surname=surname
        self.field=field
        self.id=Student.ID
        Student.ID+=1
    def __str__(self):
        return f"{self.name} {self.surname}({self.id}), {self.field}"
w=Student("Max","Malich","AI")
q=Student("gd","ewf","gwe")
e=Student("rex","peks","logistyka")
print(q)
print(e)
print(w)