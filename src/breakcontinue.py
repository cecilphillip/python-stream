# Python file names.py
names = ["Jimmy", "Rose", "Max", "Nina", "Phillip"]

def do_stuff():
    for name in names:
        print(f'We are in the outer loop {name}')
        for char in name:
            if char == 'x':
                print(f'Found target letter in {name}')
                return
        else:
            print(f'Did not find target in {name}') # if does not break
    print('End of all the loops')

do_stuff()


# for name in names:
#     if len(name) != 4:
#         continue
#     print(f"Hello, {name}")
#     if name == "Nina":
#         break
# print("Done!")
