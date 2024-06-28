class Calculator():
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        if self.y!=0:
            return self.x/self.y
        else:
            print("Denominator cannot be zero")

n1=int(input("Enter the first integer: "))
n2=int(input("Enter the second integer: "))

calculator=Calculator(n1,n2)
choice=1
while choice!=0:
    
    print("\n0.Exit \n1.Add \n2.Subtract \n3.Multiply \n4.Divide")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print(f"\nThe result of Addition is: ",calculator.add())
    elif choice==2:
        print(f"\nThe result of Subtraction is: ",calculator.sub())
    elif choice==3:
        print(f"\nThe result of Multiplication is: ",calculator.mul())
    elif choice==4:
        print(f"\nThe result of Division is: ",calculator.div())
    elif choice==0:
        print("\nYou have exited successfully")
        break
    else:
        print("\nInvaid choice!!!")
print()