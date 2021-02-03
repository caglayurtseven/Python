# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the
# even-valued terms.

total=0
fib1=1
fib2=1

fib=fib1+fib2
while(fib<4000000):
    if(fib%2==0):
        total+=fib
    fib1=fib2
    fib2=fib
    fib=fib1+fib2

print(total)