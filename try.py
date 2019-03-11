try:
	a=int(input("enter nuber"))
	if a<3:
		b=int((a/a-3))
	elif a==3:
		raise ZeroDivisionError
	else:
		raise NameError
except ZeroDivisionError:
	print("some error occured")
except NameError:
	print("u have choosena number greater than 3")
else:
	print(b)