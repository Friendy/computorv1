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
# def round6(n):
# 	print("n", n)
# 	nString = str(abs(n))
# 	point = nString.find(".")
# 	if (len(nString) - point - 1) <= 7: # check !!!
# 		if abs(int(n) - float(n)) == 0:
# 			return int(n)
# 		return n
# 	digit = int(nString[point + 7])
# 	int_part = int(nString[:point])
# 	float_part = int(nString[point + 1 : point + 7])
# 	print("float", float_part)
# 	if digit >= 5:
# 		float_part = float_part + 1
# 	print("change float", float_part, digit)
# 	result = int_part + float_part * 0.000001
# 	print("res", result)
# 	if n < 0:
# 		result = -result
# 	return result

def round6(n):
	nString = str(abs(n))
	point = nString.find(".")
	if (len(nString) - point - 1) <= 7: # check !!!
		if abs(int(n) - float(n)) == 0:
			return int(n)
		return n
	digit = int(nString[point + 7])
	int_part = int(nString[:point])
	float_part = int(nString[point + 1 : point + 7])
	if digit >= 5:
		float_part = float_part + 1
	string_result = f"{int_part}.{float_part}"
	result = float(string_result)
	if n < 0:
		result = -result
	return result