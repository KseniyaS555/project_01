# Задача 2.1.

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [`-52, 56, 30, 29, -54, 0, -110`] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    pass
    i = 0
    n=len(arr)
    
    while i < n - 1:
        m = i
        j = i + 1
        while j < n:
            if int(arr[j]) < int(arr[m]):
                m = j
            j += 1
        arr[i], arr[m] = arr[m], arr[i]
        i += 1
    min=arr[0]
    return min
def maximum(arr):
    pass
    i = 0
    n = len(arr)
    #print(n)
    while i < n - 1:
        m = i
        j = i + 1
        while j < n:
            if int(arr[j]) < int(arr[m]):
                m = j
            j += 1
        arr[i], arr[m] = arr[m], arr[i]
        i += 1
    max=arr[-1]
    return max
a=input('Введите целые числа через запятую : ').split(',')
arr=a

print(arr,"      -> max = " ,maximum(arr),"min = ", minimum(arr))

