def even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

input = int(input("Enter a number: "))
if even_odd(input):
    print(f"The Number {input} is even.")
else:
    print(f"The Number {input} is odd.")
