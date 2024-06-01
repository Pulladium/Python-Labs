"""
Homer's fridge
Course: B0B36ZAL
"""

#nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration
#predesly kod nijak nemodifikujte!

def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
# openFridge(fridge)


"""
Task #1
"""
def maxExpirationDay(fridge):
    if fridge is None or len(fridge) == 0:
        return -1
    else:
        max = fridge[0].expiration
        for food in fridge:
            if food.expiration > max:
                max = food.expiration
        return max

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(maxExpirationDay(fridge))
# The command should print 4


"""
Task #2
"""
def histogramOfExpirations(fridge):
    histogram = [0] * (maxExpirationDay(fridge) + 1)
    for exp in range(len(histogram)):
        for food in fridge:
            if food.expiration == exp:
                histogram[exp] += 1

    return histogram

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(histogramOfExpirations(fridge))
# The command should print [0, 2, 0, 1, 1]


"""
Task #3
"""
def cumulativeSum(histogram):
    sum = [0] * len(histogram)
    for i in range(len(histogram)):
        for j in range(i+1):
            sum[i] += histogram[j]
    return sum

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(cumulativeSum([0, 2, 0, 1, 1]))
# The command should print [0, 2, 2, 3, 4]


"""
Task #4
"""
def sortFoodInFridge(fridge):
    sort_fridge = [None] * len(fridge)
    kumSum = cumulativeSum(histogramOfExpirations(fridge))
    for food in fridge:
        i = food.expiration
        kumSum[i] -= 1
        poslnd = kumSum[i]
        sort_fridge[poslnd] = food
    return sort_fridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #5
"""
def reverseFridge(fridge):
    new_fridge = [None] * len(fridge)
    for i in range(len(fridge)):
        x = len(fridge)-i-1
        new_fridge[i] = fridge[x]
    return new_fridge   

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(reverseFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #6
"""
def eatFood(name, fridge):
    # sorted = sortFoodInFridge(fridge)
    new = fridge.copy()
    if new is None or len(new) == 0:
        return new
    curr_exp = None
    curr_food = None
    for food in new:
        if food.name == name:
            if(curr_exp is None or curr_exp > food.expiration):
                curr_food = food
                curr_exp = food.expiration

    if curr_food is not None:
        new.remove(curr_food)
    return new
            # curr_exp = food.expiration

            # sorted.remove(food)
            # return sorted

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(
#     eatFood("donut",
#         [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#         Food("donut", 3), Food("donut", 1), Food("donut", 6)]
#     ))
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)
