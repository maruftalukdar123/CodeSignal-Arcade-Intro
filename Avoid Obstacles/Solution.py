import numpy as np
def solution(obstacles):
    if len(obstacles)==0:
        return 1

    possible_numbers = [i for i in range(max(obstacles)+1) if i not in obstacles]
    
    possible_paths = []
    for i in range(1,max(obstacles)+1):
        path = np.arange(0,max(obstacles)+1,i)
        possible_paths.append(path)

    x = [ [] for i in range(len(possible_paths)) ]
    
    for i in range(len(possible_paths)):
        for j in possible_paths[i]:
            x[i].append(j in possible_numbers)
    
    for i in range(len(x)):
        if all(x[i]):
            return i+1
    
    return max(obstacles)+1
    



    # possible_paths = []
    # for i in range(1,len(obstacles)):
    #     path = np.arange(0,obstacles[-1],i)
    #     possible_paths.append(path)

    # possible_paths_to_remove = []
    # for index, i in enumerate(possible_paths):
    #     for j in i:
    #         if j in obstacles:
    #             possible_paths_to_remove.append(index)
    #             break
    
    # for i in range(len(possible_paths_to_remove)):
    #     if i not in possible_paths_to_remove:
    #         return i+1

