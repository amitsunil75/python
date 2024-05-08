class MyDetails:
    def __init__(self,name,age,email):
        self.name=name
        self._email=email
        self.age=age
    def myemail(self):
        return self._email.lower()
    
    def myName(self):
        return self.name
    def myAge(self):
        return self.age
        

myDetails =MyDetails('amit',20,'Amitsunil@gmail.com')
print('my name is',myDetails.myName())
print('my email is',myDetails.myemail())
print('my age is ',myDetails.myAge())
