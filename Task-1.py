dict = {
    "Lakshya" : 21,
    "Ritik" : 20,
    "Ankit" : 22,
    "Anshul" : 19,
    "Divyansh" : 18
}

user_input = input("Want to retrieve Marks of any student? (yes/no) ")

try:
    if user_input == "yes":
        name = input("Enter the student's name : ").capitalize()
        print(f"{name}'s marks is {dict[name]}")
    elif user_input == "no":
        print("Okay")
    else:
        print("Answer in yes or no only!")
        
except Exception as e:    
    print(f"Error: " + type(e).__name__)