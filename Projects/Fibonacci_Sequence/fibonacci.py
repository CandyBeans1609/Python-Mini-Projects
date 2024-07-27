def fibo(n):
    print("====The fibonacci sequence is: ====")
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
    

n = 10  
for num in fibo(n):
    print(num)


