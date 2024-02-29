# Given a Integer array A[] of n elements.
# Your task is to complete the function PalinArray.
# Which will return 1 if all the elements of the Array are palindrome
# otherwise it will return 0.

# Example 1:
# Input:
# 5
# 111 222 333 444 555

arr = [111, 223]

def PalinArray(arr):
    bool_list = []
    for numb in arr:
        pal = (str(numb) == str(numb)[::-1])
        bool_list.append(pal)
    print(bool_list)
    return all(bool_list)





numb_111 = 111
type(numb_111)
