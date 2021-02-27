while True :
    print("options:")
    print("type add to Add:")
    print("type sub to subtract :")
    print("type div to divide:")
    print("type mul to multiply:")
    print("type quit to break:")
    user_input = input(": ")
    print(user_input)
    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input(": "))
        num2 = float(input(": "))
        result = num1 + num2
        print(result)
    elif user_input == "sub":
        num1 = float(input(" : "))
        num2 = float(input(": "))
        result = num1 - num2
        print(result)
    elif user_input == "div":
        num1 = float(input(": "))
        num2 = float(input(": "))
        result = num1 / num2
        print(result)
    elif user_input == "mul":
        num1 = float(input(": "))
        num2 = float(input(": "))
        result = num1 * num2
        print(result)
    else :
        print("unknown input")
        break