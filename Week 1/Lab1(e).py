n = int(input("enter number of terms: "))
def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print("Fibonacci series: ")
for i in range(n):
    print(fibonacci(i), end=" ")
