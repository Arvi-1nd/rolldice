import random

count = 0

while True:
    try:
       dice_choice = int(input("How many dice? "))
       if dice_choice <= 0:
          print("invalid choice! please enter positive number")
          continue
    except ValueError:
         print("Invalid input")
         continue
         
    choice = input("Roll dice? (y/n): ").lower()
    
    if choice == 'n':
       print("Thanks for playing!")
       break
   
    elif choice == 'y':
       count += 1
       print(f"count:{count}")
       rolls = [random.randint(1,6) for _ in range(dice_choice)]
       print(f"Rolls:{tuple(rolls)}")
       
    else:
       print("invalid input!,please enter 'y'  or 'n' ")



