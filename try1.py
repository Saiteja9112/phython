try:
	l=[1,2,3,4,5,6]
	a=int(input("enter nuber"))
	print(l[a])
except :
	print("index is out of range")
else:
	print("successfully exicuted")
finally:
	print("completed")