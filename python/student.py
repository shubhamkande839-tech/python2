class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    
    def display(self):
        print("name:",self.name)
        print("roll No:",self.rollno)

s1=student("om",101)

s1.display()
