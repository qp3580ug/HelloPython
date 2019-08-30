user_phrase = str(input("Please enter a phrase: "))

print(user_phrase[0].lower()+user_phrase[1:].title().replace(" ", ""))