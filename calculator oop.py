class calculator:
    def _init_(self):
        pass
    def addition(self, x, y):
        return x+y
    def subtraction(self, x, y):
        return x-y
    def multiplication(self, x, y):
        return x*y
    def division(self, x, y):
        if y == 0 :
            return "cannot be divided by ZERO"
        return x/y
    
cal = calculator()

while True :
    print("Select Operation :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    select_operation = input("Enter Option (1/2/3/4/5) : \n")

    if select_operation == '5':
        print("Thank you")
        break

    
    if select_operation in ('1','2','3','4') :
        num1 = float(input("Input number to 1 : "))
        num2 = float(input("Input number to 2 : "))

        if select_operation == '1' :
            print("perform addition operation : ", cal.addition(num1, num2))
        
        elif select_operation == '2' :
            print("perform subtraction operation : ", cal.subtraction(num1, num2))
        
        elif select_operation == '3' :
            print("perform multiplication operation : ", cal.multiplication(num1, num2))
        
        elif select_operation == '4' :
            print("perform division operation : ", cal.division(num1, num2))
    
    else :
        print("your choice is invalid !")