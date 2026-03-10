
# функция получает отсортированный массив и значение
def binary_search(list: list, item: int) -> int | None:
    # в low и high хранятся границы той части списка, в которой выполняется поиск
    low = 0
    high = len(list) - 1
    
    # пока эта часть не сократится до одного элемента проверяем средний элемент
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return guess
        
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

    
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 6))