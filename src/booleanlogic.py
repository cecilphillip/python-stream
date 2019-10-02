is_it_monday = False
is_today_wednesday =  True

default = {'name': 'Brian'}
cecil = {'name': 'Cecil'}
apples_i_really_want = {}

def get_apples():
    # get user data from database
    return apples_i_really_want or default

result = get_apples()

print(result)

