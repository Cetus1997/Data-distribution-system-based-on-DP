# This original data distribution system
import random
import math

capacity = 1  # the capacity of the knapsack
queryNum = 20  # the number of the queries

epsilon = 1 / 3
count = [0, 0]
totalValue = [0, 0]
copyList = []
L = 1
U = 2


def randomQuery(num):  # epsilon:the max privacy budget requested by users
    query = []
    for i in range(num):
        query_i = [0, 0]
        weight = random.uniform(0, epsilon)
        value = random.uniform(weight * L, weight * U)
        query_i[0] = weight
        query_i[1] = value
        query.append(query_i)
    return query


def oldMethod(query, remain):
    flag = False
    if query[0] < remain:
        flag = True
    return flag


def newMethod(query, remain):
    flag = False
    if query[0] < remain:
        density = query[1] / query[0]
        Threshold = math.pow((U * math.e / L), (1 - remain)) * (L / math.e)
        if density >= Threshold:
            flag = True
    return flag


def main():
    queryList = randomQuery(queryNum)
    valueSum = 0  # value sum of all queries
    weightSum = 0  # weight sum of all queries
    remain = [1, 1]
    for query in queryList:
        valueSum += query[1]
        weightSum += query[0]
        if oldMethod(query, remain[0]):
            count[0] += 1
            totalValue[0] += query[1]
            remain[0] = remain[0] - query[0]
        if copyList and query[0] < max(copyList):  # copy can be reused
            totalValue[1] += query[1]
            count[1] += 1
        elif newMethod(query, remain[1]):
            copyList.append(query[0])
            remain[1] = remain[1] - query[0]
            count[1] += 1
            totalValue[1] += query[1]
    ratio = valueSum / totalValue[1]
    print(count, totalValue, ratio, valueSum, weightSum)


if __name__ == '__main__':
    main()
