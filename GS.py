import math

def dot(v1, v2):
    i = 0;
    result = 0;
    while (i < len(v1)):
        result = result + (v1[i] * v2[i])
        i = i + 1
    return result

def sub(v1, v2):
    i = 0
    result = []
    while (i < len(v1)):
        result.append(v1[i] - v2[i])
        i = i + 1
    return result

def mul(c, v1):
    i = 0
    result = []
    while (i < len(v1)):
        result.append(c * v1[i])
        i = i + 1
    return result
    
def GS_helper(vector, orth, index):
    save = vector[index]
    front = 0
    while (front < index):
        up = dot(vector[index], orth[front])
        down = dot(orth[front], orth[front])
        div = up / down
        save = sub(save, mul(div, orth[front]));
        front = front + 1
    return save

def unify(v):
    i = 0
    result = []
    while (i < len(v)):
        unit = math.sqrt(dot(v[i], v[i]))
        j = 0
        while (j < len(v[i])):
            result.append(v[i][j] / unit)
            j = j + 1
        i = i + 1
    return result
    
def GS(v):
    i = 0
    answer = []
    while (i < len(v)):
        answer.append(GS_helper(v, answer, i));
        i = i + 1
    return unify(answer)
    
print(GS([[3,5],[4,-7]]));
print(GS([[3,5,1],[4,-7, 2], [4, 7,8]]));