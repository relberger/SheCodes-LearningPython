def print_stars(num_stars):
    print("*" * num_stars)

def print_triangle(num_rows):
    for num in range(num_rows):
        print_stars(num)

print_triangle(6)

def print_trapeze(num_rows):
    for num in range(5, num_rows):
        print_stars(num)

print_trapeze(9)

def print_diamond(num_rows):
    for num in range(num_rows):
        print_stars(num)
    while num > 0:
        num = num - 1
        print_stars(num)

print_diamond(4)