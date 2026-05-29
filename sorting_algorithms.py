#bubble_sort

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


my_list = [64, 34, 25, 12, 22, 11, 90, 0]
bubble_sort(my_list)
print("Отсортированный список:", my_list)


#insertion_sort

def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


my_list = [64, 34, 25, 12, 22, 11, 90, 0]
insertion_sort(my_list)
print("Отсортированный список:", my_list)


#selection_sort


def selection_sort(arr):
    for step in range(len(arr)):
        min_index = step
        for i in range(step + 1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i

        (arr[step], arr[min_index]) = (arr[min_index], arr[step])


my_list = [64, 34, 25, 12, 22, 11, 90, 0]
selection_sort(my_list)
print("Отсортированный список:", my_list)

