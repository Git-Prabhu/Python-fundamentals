def double_even_indices (lst):
    '''(list of int) -> NoneType
    Double very other int in lst, starting at index 0.
    '''

    i = 0
    while i < len(lst):
        lst [i] = lst [i] * 2
        i = i + 2

list1 = [11, 12, 13, 14, 15, 16, 17]
print (list)
double_even_indices (list1)
print (list1)
