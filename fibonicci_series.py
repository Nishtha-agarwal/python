def fib(n) : # Write fibonicci series upto n
    a, b = 0, 1
    while b < n:
        print(b),
        a, b = b, a+b
#now call func we just defined:    
fib(10000)
print("Fibonicci series upto n.")
