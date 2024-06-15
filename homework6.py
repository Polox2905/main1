my_dict = {"Paul": 1984, "Anton": 1985, "Sergey": 1983, "Anna": 1978}
print("Dict", my_dict)
print("Existig value", my_dict.get("Paul"))
print("None existig value", my_dict.get("Alise"))
my_dict["Vera"]=1965
my_dict.update({"Uriy": 1980, "Evgeniy": 2000})
a = my_dict.pop("Sergey")
print("Deleted value", a)
print("Modified dict", my_dict)
my_set = {1, 4, 6, 1, 7, 8, 7, 4, 10}
print("Set", my_set)
my_set.discard(1)
my_set.add(True)
print("Modified set", my_set)




