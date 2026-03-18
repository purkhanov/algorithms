# Bubble sort

def bubble_sort(arr: list):
    n = len(arr)
    while True:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
        n -= 1
        
my_list = [4, 1, 0, 3, 2]
my_list = [4, 0, 1, 2, 3]
bubble_sort(my_list)

print(my_list)