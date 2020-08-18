def fizzbuzz_convert(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)


# num = int(input('1つの自然数を入れてください:'))

r = fizzbuzz_convert(1)
print(r)
