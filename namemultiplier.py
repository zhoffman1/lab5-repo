name = input("ENTER YOUR NAME ?> ")
while true:
    try:
        times = int(input("ENTER YOUR MULTIPLIER ?> "))
        if (times <= 0): 
            print("YOUR MULTIPLIER MUST BE GREATER THAN ZERO!")
            continue
        for i in range(times):
            print(f"Your name is {name}!!! HA HA HA")
            break
    except ValueError as e:
        print(e)
        continue
