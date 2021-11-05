unsorted_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("The unsorted list: " + str(unsorted_list))
sorted_list = unsorted_list
sorted_list.sort()
print("Ascending order: " + str(sorted_list))
sorted_list.reverse()
print("Descending order: " + str(sorted_list))
sorted_list.reverse()
print("Even numbers: " + str(sorted_list[1::2]))
print("Odd numbers: " + str(sorted_list[0::2]))
print("Multiples of 3: " + str(sorted_list[2::3]))
