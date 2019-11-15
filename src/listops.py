names = ['Cecil', 'Brian', 'Michael', 'Edna', 'Gertrude', 'Lily', 'Beverly']
#result = []

# for name in names:
#     result.append(len(name))

def cap(name):
    up = name.upper()
    reversed_list = list(reversed(up))
    return "".join(reversed_list)

result = [cap(name) for name in names]



print(result)
