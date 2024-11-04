''''
qustion 1
DESCRIPTION
 This is a pyhthon program that asks the user for their name and replies with a personalised greeting. The same program then asks the 
 user to enter their age and then calculates the year they where born basing on the current year which is 2024 
'''

# Prompt the user to enter their name
user_name = input('Hello I am Ketra. Please enter your name: ')

# Greets the user by name and ask how they are doing
print(f'Hello there {user_name} How are you this wonderful day?')

# Instruct the user that they can reply or press enter to continue
print("(You can reply or press enter to continue...)")

# Capture the user's response and convert it to lowercase for easier comparison
user_reply = input().lower()

# Check if the user has provided any non-whitespace input
if user_reply.strip(): 
    # List of positive replies
    positive_replies = [
        "good", "great", "awesome", "fantastic", "excellent", 
        "wonderful", "cool", "happy", "amazing", "perfect", 
        "lovely", "super", "terrific", "feeling great", 
        "I am doing well", "all good", "not bad", "excited", 
        "thrilled", "blessed"
    ]
    
    # List of negative replies
    negative_replies = [
        "bad", "not good", "terrible", "awful", "horrible", 
        "sad", "unhappy", "disappointing", "frustrating", 
        "rough", "boring", "poor", "up and down", 
        "not great", "just"
    ]

    # Check if the user's reply contains any positive keywords that might have been put in the list for positive replies
    if any(response in user_reply for response in positive_replies):
        # Respond positively
        print("That is really nice")
    
    # Check if the user's reply contains any negative keywords that might have been entered in the negative reply
    elif any(response in user_reply for response in negative_replies):
        # Respond sympathetically
        print("I'm sorry to hear that. I will keep you in prayer")
    
    # If the reply doesn't match positive or negative categories
    else:
        # Encourage the user to share more
        print("Thanks for sharing!")

# Introduce the next part of the interaction regarding the user's age
print(f'Now {user_name}, I want to show you all my capabilities. Let’s do something; just tell me your age and I will tell the year in which you were born')

# Instruct the user to press enter to continue
print("(Press enter to continue...)")

# Wait for the user to press enter
input()

try:
    # Prompt the user to enter their age and convert it to an integer
    user_age = int(input('Enter your age: '))

    # Calculate the year of birth based on the current year (2024)
    results = 2024 - user_age

    # Output the calculated birth year to the user
    print(f'Guess what {user_name}, your year of birth is {results}')
    print("(Press enter to continue...)")
    input()
except ValueError:
   print('This is an invalid input please enter a number')

# end


# question 2 continuation of the first one
'''
In the next part the program continues to ask the user for their favourite number to determine 
wheather its even or odd and then depending on the user's input, the program gives a response if 
the numberif the number entered is greater than,less than or eqaul to ten
'''
print(f'Now {user_name}, lets try something else. You are going to give me a random number which I will analyze and tell you whether it\'s an even number or an odd number.')
print("(Press enter to continue...)")
input()

try:
    user_number = int(input(f'OK {user_name} give me the number: '))
    
    # Determine if the number is even or odd
    user_input = user_number % 2
    
    if user_input == 0:
        print(f' {user_name}, {user_number} is an even number')
    else:
        print(f'{user_name},{user_number} is an odd number')
    
    # Check if the number is greater than, less than, or equal to ten
    if user_number > 10:
        print(f'{user_name},{user_number} is greater than ten')
    elif user_number < 10:
        print(f'{user_name},{user_number} is less than ten')
    else:
        print(f'{user_name},{user_number} is equal to ten')

except ValueError:
    print('This is an invalid input please enter a valid integer')

    class Book:
        def __init__(self, title, author, year_published):
            self.title = title
            self.author = author
            self.year_published = year_published

        def description(self):
            return f"{self.title} by {self.author}, published in {self.year_published}"


# Instantiate two Book objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)

# Display their descriptions
print(book1.description())
print(book2.description())

