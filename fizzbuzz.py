def fizzbuzz_convert(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


# num = int(input('1つの自然数を入れてください:'))

r = fizzbuzz_convert(1)
print(r)
