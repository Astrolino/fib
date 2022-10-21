import math  
def fact(n):  
    return(math.factorial(n))  


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
    
 
        
factorial(5)
fact(5)
