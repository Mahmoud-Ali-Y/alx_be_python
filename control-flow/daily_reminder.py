task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match Priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high priority task that requires your attention!")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that requires respective attention today!")
        else:
            print(f"{task} is a medium priority task that requires respective attention once you have time!")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task. Consider completing it once you can.")
        else:
            print(f"{task} is a low priority task. Consider completing it when you have free time.")
