def introspection_info(obj):

    type_of_object = type(obj)

    attributes = dir(obj)

    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    try:
        module = obj.__module__
    except AttributeError:
        module = "__main__"

    info = {
        'type': type_of_object.__name__,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }

    return info

number_info = introspection_info(42)
print(number_info)
















