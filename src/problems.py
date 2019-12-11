from colorama import Fore, Style

exp = (ValueError, TypeError)
try:
    result = int('hghg')
    print(f'{Fore.BLUE}{result}')
except exp:
    print(Fore.RED + 'Invalid format provided.')
except Exception as ex: # This is just a demo. DON'T DO THIS!
    print(Fore.RED + 'Bad stuff happened that we didn\'t expect')
else:
     print('Assuming that an exception didn\'t fire')
finally:
    print(Fore.GREEN + 'We ALWAYS get to the finish.')

print('Will you be there?')
