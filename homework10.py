my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    current_number = my_list[index]
    if current_number < 0:
        break
    if current_number == 0:
        index += 1
        continue
    print(current_number)
    index += 1

#    if current_number < 0:
#        index += 1
#        continue
#    if current_number == 0:
#        index += 1
#        continue
#    print(current_number)
#    index += 1