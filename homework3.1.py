calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    global calls
    count_calls()
    str1 = len(string)
    str2 = string.upper()
    str3 = string.lower()
    return str1, str2, str3

def is_contains(string, list_to_search):
    global calls
    count_calls()
    string = string.lower()
    return string in map(str.lower, list_to_search)

print(string_info("capibara"))
print(string_info("armagedon"))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)










