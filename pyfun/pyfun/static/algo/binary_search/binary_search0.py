# array: sorted array asc of comprable type
# n: length of the array
# key: search query
def binary_search(array, key):
    n = len(array)
    r = n-1
    l = 0
    while l <= r:
        m = int((l + r)/2)
        if array[m] < key:
            l = m + 1
        elif array[m] > key:
            r = m - 1
        else:
            return m
    return -1

if __name__ == "__main__":
    a = [1, 7, 4, 3, 8, 9, 0, -1]
    key = 7
    print('array: ' +  a.__str__())
    a.sort()
    print('sorted: ' +  a.__str__())
    print('key: ' +  str(key))
    print('index: ' + str(binary_search(a, key)))