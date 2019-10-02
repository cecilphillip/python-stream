from colorama import Fore, Style

try:
    result = int('hghg')
    print(f'{Fore.BLUE}{result}')
# except (ValueError, TypeError):
#     print(Fore.RED + 'Invalid format provided.')
# except Exception as ex:
#     print(Fore.RED + 'Bad stuff happened that we didn\'t expect')
# else:
#     print('Assuming that an exception didn\'t fire')
finally:
    print(Fore.GREEN + 'We ALWAYS get to the finish.')

print('Will you be there?')
