def TwoDToOneD(TwoDArr):
    arr = []
    for i in range(len(TwoDArr)):
        for j in range(len(TwoDArr[i])):
            arr.append(TwoDArr[i][j])

    return arr

print(TwoDToOneD([[1,2,3],[4,5,6],[1,2]]))