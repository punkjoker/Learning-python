def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

num=int(input("Enter a number:"))
result=check_even_odd(num)
print(f"The number {num} is {result}.")
