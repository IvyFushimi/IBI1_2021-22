#ZJE human resources databases
class Staff (object):#start a class
    def __init__(self,f,l,r):
        self.fullname = f#input the full name of the staff
        self.location = l#input the location
        self.role = r#input the role
    def staff(self):
        print(self.fullname,self.location,self.role)
#for example, I had put in a piece of information
staff1 = Staff('Ouyang_Hongwei','International_Campus','dean')
staff1.staff()
