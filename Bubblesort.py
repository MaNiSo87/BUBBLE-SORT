def Bubble_Sort(numbers_list):
    for i in range (1, len(numbers_list)):
        for j in range(len(numbers_list) - i):
            if int(numbers_list[j]) > int(numbers_list[j + 1]):
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
    return numbers_list
 
list = Bubble_Sort(input('Entre your numbers: ').split())
for i in list:
    print(int(i), sep='', end=' ')
