#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#Make sure your program works on two lists of different sizes. + at least one list comprehension 
def listoverlap2(lst1, lst2):
    return set([ x for x in lst1 if x in lst2 ])

a = [1, 1, 2, 3, 3, 3 ,3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3 , 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(listoverlap2(a,b))