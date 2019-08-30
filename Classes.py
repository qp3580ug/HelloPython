numberOClasses = int(input("How many classes are you taking this semester? "))
class_list =[]

for c in range(numberOClasses):
    new_class = input("Enter name of class: ")
    class_list += [new_class]

for c in class_list:
    print(c)