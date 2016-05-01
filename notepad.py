# tworzenie listy za pomoca range()
my_list = range(5, 51)
print my_list

# tworzenie listy za pomoca petli
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 ==0]
print cubes_by_four

# odwracanie kolejnosci listy
my_list = range(1, 11)
backwards = my_list[::-1]

for i in range(1,257):
    print i, ":", bin(i)
