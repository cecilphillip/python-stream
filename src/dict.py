# creating a dictionary

empty_dict = {}

states = {
    "FL" : "Florida",
    "NY" : "New York"
}

phone_book = {
    "Brian" : "555-555-6666",
    "Cecil" : "321-124-1231"
}

int_value = 1
string_value = "some string"
list_value = [1,2,4]
tuple_value = (1,2,3)
dict_value = {1: "one", "tw0" : 2}
set_value = {"Brian", "Cecil", "Shayne"}

crazy_twitch_dictionary = {
    int_value : list_value,
    string_value : "twitch",
    tuple_value : tuple_value
}

print(int_value)
print(crazy_twitch_dictionary)
int_value = 2
print(crazy_twitch_dictionary)

