def pow2(n):
	return n*n

def square_root(n):
	if n == 1:
		return 1
	if n > 1:
		min = 0
		max = n
	else:
		min = n
		max = 1
	candidate = min + (max - min)/2
	temp_pow = pow2(candidate)
	while (temp_pow != n):
		if temp_pow > n:
			max = candidate;
		else:
			min = candidate;
		old_candidate = candidate
		candidate = min + (max - min)/2
		if candidate == old_candidate:
			return candidate
		temp_pow = pow2(candidate)
	return candidate

# rounds till 6 digits after the point
def round6(n):
	nString = str(abs(n))
	point = nString.rfind(".")
	# print("point", point, len(nString), nString)
	if (len(nString) - point - 1) <= 7: # check !!!
		return n
	digit = int(nString[point + 7])
	nString = nString[:point + 7]
	result = float(nString)
	if digit >= 5:
		result = result + 0.000001
	if n < 0:
		result = -result
	return result 