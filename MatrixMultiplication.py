matrix_1 = [[22,5,12]],[[15,4,20]]
matrix_2 = [[8,2]], [19,3], [13,7]]

def multiply(matrix_1, matrix_2):
    result = []
    for i in range(len(matrix_2[0])): 
        total = 0
        for j in range(len(matrix_1)):
            total += matrix_1[j] * matrix_2[j][i]
        result.append(total)
    return result
    print str(result)
