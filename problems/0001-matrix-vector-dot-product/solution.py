def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a) != len(b):
		return -1
	ans = []
	for x in a:
		calc = 0
		for y in range(len(x)):
			calc += (x[y] * b[y])
		ans.append(calc)
	return ans