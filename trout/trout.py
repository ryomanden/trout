import numpy as np
import sympy as sp

def inverse(data,mod):
    data = np.array(data, dtype=int)

    #--- 行列式計算 ---#
    det = np.linalg.det(data)
    det = int(det % mod) #modかける
    det_inv = sp.gcdex(det,mod)[1]
    #--- ひっくり返す(いい感じじゃない) ---#
    tmp = data[0][0]
    data[0][0] = data[1][1]
    data[1][1] = tmp

    tmp = data[0][1]
    data[0][1] = data[1][0]*(-1)
    data[1][0] = tmp*(-1)

    data_inv = np.dot(data, det) % mod

    return data_inv


#関数化うまくいってない#
def euclid(a,b):
    a: int = []
    b: int = []
    r: int = []
    q: int = []

    #input
    a.append(a)
    b.append(b)

    if 0 == a[0] or 0 == b[0]: #Check suitability
        raise Exception('ERROR: Unsupported Zero')

    i = 0

    #Euclid
    while True:
        q.append(a[i] // b[i])
        r.append(a[i] % b[i])
        print('  ', a[i], '=', b[i], '×', q[i], '+', r[i])

        if r[i] == 0:
            break
        a.append(b[i])
        b.append(r[i])
        i += 1
    
    return b[i] 
    