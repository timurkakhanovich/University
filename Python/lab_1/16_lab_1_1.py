def fib(num):
	fib_res, fib_temp = 0, 1
  
	for _ in range(num):
		# Swapping two numbers:  
		# fib_res contains the penalt value,  
		# fib_temp contains the last value.  
		fib_temp, fib_res = fib_res + fib_temp, fib_temp
		
	return fib_res

def main():
	num = int(input("Enter the n-s number of Fibonacci: "))

	if num >= 0:
		print("The result is {num}".format(num=fib(num)))
	else:
		print("This function takes only non-negative numbers!")

if __name__ == "__main__":
	main()
