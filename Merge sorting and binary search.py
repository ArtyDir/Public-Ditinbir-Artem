def merge_sort(L): 
    if len(L) < 2:  
        return L[:]
    else:
        middle = len(L) // 2 
        left = merge_sort(L[:middle]) 
        right = merge_sort(L[middle:])
        return merge(left, right) 
    
def merge(left, right): 
    result = [] 
    i,j = 0,0 
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
        
    while j < len(right):
        result.append(right[j])
        j += 1
        
    return result

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    elif array[middle] != element:
        print("Число не соответствует заданному условию")
    else:
        return binary_search(array, element, middle + 1, right)

sequence_of_numbers = input("Введите последовательность чисел через пробел: ")

element = int(input("Введите любое число из ранее введеных: "))

sequence_of_numbers_list = list(map(int, sequence_of_numbers.split()))

sorted_list = merge_sort(sequence_of_numbers_list)
print("Отсортированный список по возрастанию: ", sorted_list)

element_index = binary_search(sorted_list, element, 0, len(sorted_list))
print("Индекс элемента из отсортированнного списка: ", element_index)
