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
