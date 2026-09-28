import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	total_elements = sum(len(row) for row in a) if a else 0
    if total_elements != new_shape[0] * new_shape[1]:
        return []

	result = []
	z = []
	for x in a:
		for y in x:
			z.append(y)
			if len(z) == new_shape[1]:
				result.append(z)
				z = []
	return result