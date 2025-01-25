def maxWeight():
    maxWeight = int(input("What is your max weight for the exercise you are performing? "))

def week():
    max = maxWeight()
    weeknum = input("What week are you on? ")
    if weeknum == "1":
        print(f"Your sets for this week are:\n5 reps at {max * 0.65} lb,\n5 reps at {max * 0.75} lb,\nand 5+ reps at {max * 0.85} lb")
    elif weeknum == "2":
        print(f"Your sets for this week are:\n3 reps at {max * 0.7} lb,\n3 reps at {max * 0.8} lb,\nand 3+ reps at {max * 0.9} lb")
    elif weeknum == "3":
        print(f"Your sets for this week are:\n5 reps at {max * 0.75} lb,\n3 reps at {max * 0.85} lb,\nand 1+ reps at {max * 0.95} lb")
    elif weeknum == "4":
        print(f"Your sets for this week are:\n5 reps at {max * 0.4} lb,\n5 reps at {max * 0.5} lb,\nand 5 reps at {max * 0.6} lb")
        print("Please increase your max by 10 lb for upper body and 20 lb for lower body for next week.")
    else:
        print("Please input a number between 1-4 for the week you are on. If you are past week 4, please start over and increase your weight as necessary.")

