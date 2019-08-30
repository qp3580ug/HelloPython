
yourName = input("What is your name? ")
birthMonth = input("What month were you born in? ")
numberOfLetters = len(yourName)

print(f"Hello, {yourName}!")
print(f"Your name has {numberOfLetters} letters in it.")
if birthMonth.lower() == "august":
    print("Happy Birthday month!")
else:
    print(f"Your Birthday month is {birthMonth}.")