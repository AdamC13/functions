#1
def add(num1, num2):
    sol = num1 + num2
    print(sol)

def sub(num1, num2):
    sol = num1 - num2
    print(sol)

def mult(num1, num2):
    sol = num1 * num2
    print(sol)

def div(num1, num2):
    sol = num1 / num2
    print(sol)

def choose():
    op = input("Choose an operation(add, subtract, multuply, divide): ")
    try:
        num1 = int(input("Choose a number: "))
    except:
        print("Pick valid numbers!")
        pass
    try:
        num2 = int(input("Choose another number: "))
    except:
        print("Pick valid numbers!")
    
    if op == "add":
        add(num1, num2)

    elif op == "subtract":
        sub(num1, num2)

    elif op == "multiply":
        mult(num1, num2)

    elif op == "divide":
        try:
            div(num1, num2)
        except ZeroDivisionError:
            print("You fool! You can't divide by zero!")
        except TypeError:
            print("type")
    else:
        print("Enter a valid function!")

choose()

#2
a_list = []
def add_list():
    while True:
        item = input("What would you like to add to your to your shopping list?(or quit)")
        if item == "quit":
            break
        else:
            a_list.append(item)
def rem_list():
    while True:
        item = input("What would you like to remove from your shopping list?(or quit)")
        if item == "quit":
            break
        else:
            try:
                a_list.remove(item)
            except:
                print("Sorry item not found in list (┬┬﹏┬┬)")
def print_list():
    print(f"You're shopping list is {a_list}")

add_list()
rem_list()
print_list()

#3
grades1 = [85, 90, 35, 67, 84]
def avg_g(grades):
    total = sum(grades)
    print(total / len(grades))
    return total / len(grades)

def min_max(grades):
    lowest = min(grades)
    highest = max(grades)
    print([lowest, highest])
    return [lowest, highest]

def letter_g(grades):
    list_letter = []
    for grade in grades:
        if grade >= 90:
            list_letter.append("A")
        elif grade >= 80:
            list_letter.append("B")
        elif grade >= 70:
            list_letter.append("C")
        elif grade >= 60:
            list_letter.append("D")
        else:
            list_letter.append("F")
    print(list_letter)
    return list_letter

avg_g(grades1)
min_max(grades1)
letter_g(grades1)

