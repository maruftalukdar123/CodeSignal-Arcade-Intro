import numpy as np
def solution(matrix):
    
    rows = len(matrix)
    columns = len(matrix[0])

    buffer_columns = [False for i in range(columns)]

    matrix.insert(0,buffer_columns)
    matrix.append(buffer_columns)

    rows += 2
    columns += 2

    for i in range(rows-1):
        matrix[i].insert(0,False)
        matrix[i].append(False)


    answer = []
    for i in range(1,rows-1):
        row_answer = []
        for j in range(1,columns-1):
            row_answer.append(sum([ matrix[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]]))
            
            if matrix[i][j] == True:
                row_answer[j-1] -= 1
        answer.append(row_answer)
    return answer

matrix = [[True,False]]

print(solution(matrix))
            






    # rows = [ False*i for i in range(len(matrix))]
    # columns = [ False*i for i in range(len(matrix[0]))]

    # matrix = np.array(matrix)

    # matrix = np.insert(arr=matrix,obj=[0,-0],values=rows,axis=0)
    # matrix = np.insert(arr=matrix,obj=[0,-0],values=columns,axis=1)
    
    # matrix = matrix.tolist()

    # answer = []

    # for i in range(1,len(matrix)-1):
    #     for j in range(1,len(matrix[0])-1):
    #         bombs = matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1]
    #         bombs += matrix[i][j-1] + matrix[i][j+1]
    #         bombs += matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1]
    #         answer.append(bombs)
    
    # answer = np.array(answer)
    # answer = np.reshape(answer,(len(rows),len(columns)))
    # answer = answer.tolist()
    # return answer

