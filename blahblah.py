def cube(number):
    return number*number*number

def by_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return False
    

numero = int(input( "Please enter the number you want the cube of : "))
print(by_three(numero))


