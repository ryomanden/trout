import numpy as np

def inverse(data,mod):
    data = np.array(data, dtype=int)

    #--- 行列式計算 ---#
    det = np.linalg.det(data)
    det_inv = int(det % mod) #modかける

    #--- ひっくり返す(いい感じじゃない) ---#
    tmp = data[0][0]
    data[0][0] = data[1][1]
    data[1][1] = tmp

    tmp = data[0][1]
    data[0][1] = data[1][0]*(-1)
    data[1][0] = tmp*(-1)

    data_inv = np.dot(data, det_inv) % mod

    return data_inv

def euclid(a,b):
    data = [list(range(4))]
    data.insert(0, a)
    data.insert(1, b)

    if 0 == data[0] or 0 == data[1]: #Check suitability
        raise Exception('ERROR:Do not assign 0 to the 1st and 2nd argument.')
    
    i = 0
    while True:
        data[i+1][2] = (data[i][0] // data[i][1])
        data[i+1][3] = (data[i][0] % data[i][1])
        print(f'{data[i][0]} = {data[i][1]} × {data[i][2]} + {data[i][3]}')

        if data[i][3] == 0:
            break

        data[i+1][0] = data[i][1]
        data[i+1][1] = data[i][3]
        i += 1
    
    