def FizzBuzz(n):
    if n % 3 == 0 & n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0 :
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n 

for i in  range(1, 21):
    result = FizzBuzz(i)
    print(result)