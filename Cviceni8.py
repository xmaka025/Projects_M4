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
