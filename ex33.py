
numbers = []

def add_range(count):
	i = 0 
	print count
	while i < count:
		numbers.append(i)
		i = i + 1

def	print_list(list_num):
	for i in list_num:
		print i
	 
count = 10
add_range(count)

print_list(numbers)
