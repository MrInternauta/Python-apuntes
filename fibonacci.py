def fibonacci(numero):
	if numero == 0:
		return 0
	elif numero == 1:
		return 1
	else:
		return ( fibonacci(numero-1) + fibonacci(numero - 2))
if __name__ == '__main__':
    for i in range(0,8,1):
        print(fibonacci(i))
