
numbers = ['1', '10', '11', '100', '101', '110', '111']
max_digits = max(len(num) for num in numbers)
filled_numbers = [num.zfill(max_digits) for num in numbers]
print(filled_numbers,max_digits)