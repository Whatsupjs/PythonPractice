#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#Make sure your program works on two lists of different sizes.
def listoverlap(lst1, lst2):
    newlist = []

    for x in lst1: 
        if x not in newlist:
            if x in lst2:
                newlist.append(x)
    
    return newlist

a = [1, 1, 2, 3, 3, 3 ,3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3 , 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(listoverlap(a,b))