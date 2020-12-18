# 统计野餐拥有的所有食物及对应个数
allGuests = {
    'Alice': {'Apples': 5, 'Pretzels': 12},
    'Bob': {'Ham Sandwiches': 3, 'Apples': 2},
    'Carol': {'cups': 3, 'Apple Pies': 1}
}
def totalBrought(guest, item):
    numBrought = 0
    for i in guest.values():
        numBrought += i.setdefault(item, 0)
    return numBrought

food = {}
for i in allGuests.values():
    for j in i:
        food[j] = True
for k in food:
    print(' - ' + k + ' ' + str(totalBrought(allGuests, k)))

