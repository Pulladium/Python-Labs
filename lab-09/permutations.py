
def permutations(array):
    all_perms = []
    if(len(array) <= 1):
        all_perms.append(array)
        return all_perms

    cnt = 0

    for i in array:
        new = array.copy()
        new.pop(cnt)
        cnt+=1
        res = _perm(new)
        if len(res) == 1:
            res.insert(0, i)
            all_perms.append(res)
        else:
            for node in res:
                node.insert(0, i)
                all_perms.append(node)
    return all_perms
def _perm(sm_array):
    if len(sm_array) == 1:
        return sm_array
    else:
        return permutations(sm_array)

# def __perms__(array):
#     if len(array) == 1:
#         return array
#     else:
#         for
# cnt=0
# for i in permutations([]):
#     print( f"{cnt}: {i} \n")
#     cnt+=1