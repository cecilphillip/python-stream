names_list = ['Cecil', 'Brian', 'Edna', 'Gertrude', 'Beverly']
scores_list = [10, 20, 30, 2, 100]

zipped = zip(names_list, scores_list)

print(list(zipped))

scores_list.pop()

zipped = zip(names_list, scores_list)

print(list(zipped))

print(dict(zip(names_list, scores_list)))
