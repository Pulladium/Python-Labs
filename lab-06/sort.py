from collections import defaultdict
from dataclasses import dataclass



def partition(data, start, n, direct="ASC"):

    pivot = data[start]
    low = start+1
    high = n 

    while True:
        if direct == "ASC":
            while low <= high and data[high] >= pivot:
                high -= 1
            while low <= high and data[low] <= pivot:
                low += 1


            if low <= high:
                data[low], data[high] = data[high], data[low]
            else:
                break   
        elif direct == "DESC":
            while low <= high and data[high] <= pivot:
                high -= 1
            while low <= high and data[low] >= pivot:
                low += 1

            if low <= high:
                data[low], data[high] = data[high], data[low]
            else:
                break 


    data[start], data[high] = data[high], data[start]
    return high

def quick_sort(array, start, end, direct="ASC"):
    if start >= end:
        return
    
    p = partition(array, start, end, direct)

    quick_sort(array, start, p-1,direct)
    quick_sort(array, p+1, end, direct)





def sortNumbers(data, condition):
    if condition == "ASC":
        quick_sort(data, 0, len(data) - 1, 'ASC')
    elif condition == "DESC":
        quick_sort(data, 0, len(data) - 1, 'DESC')
    else:
        raise_error()   
    return data

def raise_error():
    raise ValueError('Invalid input data')


@dataclass
class My_diction_node:
    number: int
    data: list


def append2_dict(dict, num, data):
    for i in dict:
        if i.number == num:
            i.data.append(data)
            return
    dict.append(My_diction_node(number=num, data=[data]))

def get_lists(l_a, l_b):
    if(len(l_a)!= len(l_b)):
        raise_error()
        return
    
    r_dict = []

    for i in range(0, len(l_a)):
        append2_dict(r_dict, l_a[i], l_b[i])
    return r_dict

def getBynum(dict, n):
    for i in dict:
        if i.number == n:
            return i.data


def sortData(nums, list_txt, direct):
    x = get_lists(nums, list_txt)
    nums = list(set(nums))
    quick_sort(nums, 0, len(nums) - 1, direct)
    new_l = []
    for i in nums:
        for j in getBynum(x,i):
            new_l.append(j)
    
    # for i in list(set(nums)):
    #     for j in getBynum(x,i):
    #         if(direct == "DESC"):
    #             new_l.insert(0,j)
    #         elif(direct == "ASC"):
    #             new_l.append(j)
    #         else:
    #             raise_error()
    return new_l

# a =[2, 3, 4, 4, 5, 19, 2, 1] 

# a= [2, 3, 4, 4, 5, 19, 2, 1]
# b=['Praha', 'Brno', 'Pariz', 'Londyn', 'Bratislava', 'Pelhrimov', 'Jihlava', 'CB']

# new_l = sortData(a,b, 'ASC')
# print(new_l)
# b= ['Praha', 'Brno', 'Pariz', 'Londyn', 'Bratislava', 'Pelhrimov', 'Jihlava', 'CB']

# print(sortData(a,b, 'DESC'))

# print(new_l)
# print(dict_sort([2, 3, 4, 4, 5, 19, 2, 1] ,  ['Praha', 'Brno', 'Pariz', 'Londyn', 'Bratislava', 'Pelhrimov', 'Jihlava', 'CB']))
# print(sortData([2, 3, 4, 4, 5, 19, 2, 1] ,  ['Praha', 'Brno', 'Pariz', 'Londyn', 'Bratislava', 'Pelhrimov', 'Jihlava', 'CB'], 'ASC'))
# print(sortData([9.8,3,-1], ['Ford','BMW','Audi'], 'ASC'))
# print(sortData([3,0,69],['Ford','BMW','Audi'], 'DESC'))
# # manufactures = ['Ford', 'BMW', 'Audi']
# # reputation = [2, 5, 6]

# #  if condition == "ASC":
            
#         elif condition == "DESC":
#             data.sort(reverse=True)
#         else:
#             raise_error()  