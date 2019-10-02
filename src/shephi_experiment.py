name =  ["Brian"]

print(f'Original name => {name}')

def do_stuff():
    #print(name)
    name = name + "\'s"
    print(name)

do_stuff()

print(f'Has name changed {name}')
