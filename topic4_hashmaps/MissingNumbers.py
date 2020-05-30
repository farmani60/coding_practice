# Description:
# https://www.hackerrank.com/challenges/missing-numbers/problem?h_r=internal-search

def missingNumbers(arr, brr):
    arrMap = createMap(arr)
    brrMap = createMap(brr)
    lostList = []
    for k in arrMap.keys():
        if (k not in brrMap.keys()) or (brrMap[k] > arrMap[k]):
            lostList.append(k)
    return lostList


def createMap(inputArr):
    hashMap = dict()
    for i in inputArr:
        if i not in hashMap.keys():
            hashMap[i] = 1
        else:
            hashMap[i] += 1
    return hashMap


arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

print(missingNumbers(arr, brr))