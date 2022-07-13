import numpy as np
import sympy as sp

#逆行列を求める
def inverse(data,mod):
    data = np.array(data, dtype=int)

    #--- 行列式計算 ---#
    det = np.linalg.det(data)
    det = int(det % mod) #modかける
    det_inv = sp.gcdex(mod,det)[1]
    #--- ひっくり返す ---#
    tmp = data[0][0]
    data[0][0] = data[1][1]
    data[1][1] = tmp

    data[0][1] = data[0][1]*(-1)
    data[1][0] = data[1][0]*(-1)

    data_inv = np.dot(data, det_inv) % mod

    return data_inv

#連立方程式
def renritsu(data_L,data_R,mod):
    data_L = np.array(data_L, dtype=int)
    data_R= np.array(data_R, dtype=int)

    data_inv = inverse(data_L,mod)
    result = np.dot(data_inv, data_R) % mod

    return result

#RSA形式で暗号化
def rsa(mod:int,e:int,N:int,data:str):
    data = str(data)
    P = int(data, N)

    result = int(P ** e) % mod
    result = np.base_repr(result, N)
    return result


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
    