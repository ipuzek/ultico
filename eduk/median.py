# Input: N = 5
# arr[] = 90 100 78 89 67
# Output: 89
# Explanation: After sorting the array 
# middle element is the median 

ar = [90,100,78,89,67]
# sorted(ar) [67, 78, 89, 90, 100]
ari = [5,3,4,99]
# print(arr)
# type(arr)

# arr[0]

def median(arr):

    arr.sort()

    def get_middle_element(arr):
        a = arr[int(len(arr)/2)]
        return a

    def get_2_elements(arr):
        a = arr[int(len(arr)/2 - 1):int(len(arr)/2 + 1)]
        return a
    
    if (len(arr) % 2 == 1):
        ar_mid = get_middle_element(arr)
        return ar_mid

    else:
        ar_2 = get_2_elements(arr)
        return (sum(ar_2)/2)

print(ar)
print(ari)

print(median(ar))
print(median(ari))






    


