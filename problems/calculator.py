class Calculator:
    def __init__(self,a):
        result=0
        self.a=a
        # print(len(self.a))
        self.result=result

    def add(self):
        sum=0
        sum=sum+self.a
            # print(sum)
        return sum
    def sub(self):
        return self.a -self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a/self.b
    def modulus(self):
        return self.a%self.b
    def choise(self):
        choices=input('enter your choise')
        return choices
    def fetchValue(self):
        number=int(input('enter your number'))
        self.a=number
    def finish_execution(self):
        ss=input('is it over?yes')
        if(ss is 'yes'):
            exit()
        else:
            
    def showValues(self):
        myChoice =self.choise()
        if (myChoice is '+') :
            self.result = self.add()
            print(self.result)
        elif(myChoice=='-' ):
            self.result = self.sub()
    def calculate(self):
        while True:
            self.fetchValue()
            self.choise()
            self.fetchValue()

calculator =Calculator()
calculator.showValues()

