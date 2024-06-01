def polyEval(polynom, x):
    result = 0
    for i in range(len(polynom)):
        result += polynom[i] * (x ** i)
    return result

def isIndex(poly, i):
    try:
        return poly[i]
    except IndexError:
        return None
    
def polySum(poly1,poly2):
    unt = len(poly2)
    if len(poly1) >= unt:
        unt = len(poly1)
    for i in range(unt):
        if isIndex(poly1,i) == None:
            poly1.append(poly2[i])
        elif isIndex(poly2,i) == None:
            poly2.append(poly1[i])
        else: 
            poly1[i] = poly1[i] + poly2[i]
    remove0(poly1)
    return poly1

def remove0(poly):
    for i in range(len(poly)-1, 0, -1):
        if poly[i] == 0:
            poly.pop(i)
        else:
            return poly
    return poly


def polyMultiply(poly1,poly2):
    multd_poly=[]
    # Ck = S ai*bk-i
    for i in range(len(poly1)+len(poly2)):
        C_k = 0
        for k in range(i+1):
            if isIndex(poly1,k) == None:
                poly1.append(0)
            if isIndex(poly2,i-k) == None:
                poly2.append(0)
            C_k += poly1[k] * poly2[i-k]
        multd_poly.append(C_k)
    remove0(multd_poly)
    return multd_poly

# # print(polySum([1, 2, 5], [2, 0, 1, -7]))
# print(polySum([2, 0, 1, -7],[1, 2, 5]))