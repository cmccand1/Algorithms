# takes a base-10 number as an argument and returns the base-16 hexadecimal representation of that number
def decimal_to_hex(decimal_number):
    hex_values = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    result = []
    divisor = decimal_number
    while divisor != 0:
        remainder = divisor % 16
        if remainder in hex_values:
            result.append(hex_values[remainder])
        else: 
            result.append(str(remainder))
        divisor = divisor // 16
    result.reverse()
    return ''.join(result)


# test the algorithm
for i in range(0, 100000000):
    my_result = decimal_to_hex(i)
    correct_result = hex(i)[2:]
    if my_result == correct_result:
        print('Test succeeded.')
    else:
        print('Test failed. ' + 'Expected: ' + correct_result + ' Result: ' + my_result)
