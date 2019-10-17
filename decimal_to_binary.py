# takes a base-10 number as an argument and return that number in the base-2 binary representation
def division_by_two(decimal_number):
    result = []
    divisor = decimal_number
    while divisor != 0:
        if decimal_number == 0:
            result = 0
        else:
            result.append(divisor % 2)
            divisor = divisor // 2
    result.reverse()
    return ''.join(str(x) for x in result)


# test the algorithm
for i in range(0, 1000000):
    my_result = division_by_two(i)
    correct_result = bin(i)[2:]
    if my_result == correct_result:
        print('Test succeeded.')
    else:
        print('Test failed. ' + 'Expected: ' + correct_result + ' Result: ' + my_result)
