def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def get_numbers():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    return a,b

def get_operator():
    op=input("Enter the operator +,-,*,/:")
    return op

def calc(a,b, operator):
    if operator=='+':
        return add(a,b)
    if operator=='-':
        return sub(a,b)
    if operator=='*':
        return mul(a,b)
    if operator=='/':
        return div(a,b)
    else:
        return "Invalid operator"
    
def show_result(result):
    print("result=",result)
def calculator():

    a,b = get_numbers()
    operator = get_operator()

    result = calc(a,b,operator)

    show_result(result)

calculator()



