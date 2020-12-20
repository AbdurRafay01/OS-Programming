

list222 = [2,9,3,5,1]



def Sort_the_queue(list2sort : list):
    
    # list2sort = list2sort

    for i in range(1 , len(list2sort)):
        
        store = list2sort[i][2]
        
        
        j = i-1
        while j >= 0 and store < list2sort[j][2]:
            
            list2sort[j + 1] = list2sort[j]
            j -= 1
        print(list2sort[j + 1] , list2sort[i])
        list2sort[j + 1] = list2sort[i]
    
    return list2sort

print(Sort_the_queue(list2sort))



# def Sort_the_queue(lst : list):
    
    
#     return lst


# list2sort = [['P2',3,0] , ['P3',3,5] , ['P4',1,3], ['P1',23,2], ['P5',4,6]]


# print(Sort_the_queue(list2sort))