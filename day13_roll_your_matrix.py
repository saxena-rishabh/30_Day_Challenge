def toint(string_data):
    integer_data = []
    for data in string_data:
        integer_data.append(int(data))
    return integer_data

def main():
    dimension = toint(input().split())
    matrix = []
    transpose_matrix = []
    for i in range(dimension[0]):
        matrix.append(toint(input().split()))

    for i in range(dimension[1]):
        temp_row = []
        for j in range(dimension[0]):
            temp_row.append(matrix[j][i])
        transpose_matrix.append(temp_row)
    for i in range(dimension[1]):
        temp_row = ''
        for j in range(dimension[0]):
            if temp_row == '':
                temp_row = str(transpose_matrix[i][j])
            else:
                temp_row += " " + str(transpose_matrix[i][j])
        print(temp_row)
main()