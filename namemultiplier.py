name = input("ENTER YOUR NAME ?> ")
while True:
    try:
        times = int(input("ENTER YOUR MULTIPLIER ?> "))
        if (times <= 0): 
            print("YOUR MULTIPLIER MUST BE GREATER THAN ZERO!")
            continue
        print(f"Your name is {name}!!!")
        for i in range(times):
            print("HI")
        break
    except ValueError as e:
        print(e)
        continue
