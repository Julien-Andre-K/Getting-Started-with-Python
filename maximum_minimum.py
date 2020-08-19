largest = None
smallest = None

while True:

	num = input("Enter a number: ")

	if num == "done" :
		break

	try:
		num = int(num)
		if largest is None :
			largest = num
			smallest = num
		while num > largest :
			largest = num
		while num < smallest :
			smallest = num
	except:
   		print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
