def calculate_structure_sum(data_structure):
    if isinstance(data_structure, list) or isinstance(data_structure, tuple) or isinstance(data_structure, set):
        return sum(calculate_structure_sum(x) for x in data_structure)
    if isinstance(data_structure, dict):
        return sum(calculate_structure_sum(k) + calculate_structure_sum(v) for k, v in data_structure.items())
    if isinstance(data_structure, str):
        return len(data_structure)
    if isinstance(data_structure, int):
        return data_structure


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)










