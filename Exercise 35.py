humanYears = int(input("Human Age: "))
dogYears = 0

if humanYears > 2:
	dogYears = (2 * 10.5) + ((humanYears - 2) * 4)
	print("Dog years: %d" % dogYears)
elif humanYears > 0:
	dogYears = humanYears * 10.5
	print("Dog years: %d" % dogYears)
else:
	print("Error: Age cannot be negative!")