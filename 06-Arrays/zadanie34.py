def subset(arr1,arr2):

    flag = True

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                flag = True
                break
            else:
                flag = False
                
        if flag == False:
            return False

    return True

print(subset([2,3,4,5,6],[1,2,3,4,5,6]))


        