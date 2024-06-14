immutable_var=(1, 5, [4, 9], "star", True)
print(immutable_var)
# immutable_var[0]=7
# print(immutable_var)
immutable_var[2][0]=9
print(immutable_var)
mutable_list=[7, 10, "sun", False]
print(mutable_list)
mutable_list[2]="night"
print(mutable_list)
mutable_list.remove(False)
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend(["Sun", 6])
print(mutable_list)
mutable_list.extend("Sun")
print(mutable_list)