
import random
import math

capacity = 1  # the capacity of the knapsack
queryNum = 20  # the number of the queries
epsilon = 1/3
count = [0, 0]
totalValue = [0, 0]
L = 1
U = 20


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
    remain = [1, 1]
    for query in queryList:
        if oldMethod(query, remain[0]):
            count[0] += 1
            totalValue[0] += query[1]
            remain[0] = remain[0] - query[0]
        if newMethod(query, remain[1]):
            remain[1] = remain[1] - query[0]
            count[1] += 1
            totalValue[1] += query[1]
    print(count, totalValue)


if __name__ == '__main__':
    main()
