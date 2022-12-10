
def sum(a,b):
    return a + b

def sub(a,b):
    return a - b


def mul(a,b):
    return a*b 

def div(a,b):
    if b == 0 :
        raise ValueError("Cannot divide by zero")
    else:
        return a / b    

a=1
b=2

print(sum(a,b))
print(sub())