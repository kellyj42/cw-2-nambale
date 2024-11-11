# Prompt the user to enter their name
user_name = input('Hello I am Ketra. \nPlease enter your name: ')

# Greets the user by name and asks how they are feeling
print(f'Hello there {user_name} How are you this wonderful day?')

# Instructs the user that they can reply or press enter to continue
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

    # Check if the user's reply contains any positive keywords
    if any(response in user_reply for response in positive_replies):
        # Respond positively if a positive keyword is detected
        print("That is really nice")
    
    # Check if the user's reply contains any negative keywords
    elif any(response in user_reply for response in negative_replies):
        # Respond sympathetically if a negative keyword is detected
        print("I'm sorry to hear that. I will keep you in prayer")
    
    # If the reply doesn't match positive or negative categories
    else:
        # Encourage the user to share more
        print("Thanks for sharing!")

# Introduces the next part of the interaction regarding the user's age
print(f'Now {user_name}, Let’s do something, tell me your age and I will tell the year in which you were born')

# Wait for the user to press enter before continuing
input("(Press enter to continue...)")

# Loop to handle user input for age, with validation
while True:
    try:
        # Prompt the user to enter their age and convert it to an integer
        user_age = int(input('Enter your age: '))

        # Calculate the year of birth based on the current year (2024)
        results = 2024 - user_age

        # Output the calculated birth year to the user
        print(f'Guess what {user_name}, your year of birth is {results}')
        break  # Break the loop if the input is valid
        
    except ValueError:
        # Handle invalid input (non-numeric input)
        print('This is an invalid input, please enter a number')

# Now, we proceed to check if the user's number is even or odd and also compare it to 10
print(f'Now {user_name},You are going to give me a random number  and i will tell you whether it\'s an even number or an odd number.')

# Wait for the user to press enter before continuing
input("(Press enter to continue...)")

# Loop to handle user input for a number, with validation
while True:
    try:
        # Prompt the user to enter a number
        user_number = int(input(f'OK {user_name} give me the number: '))
        
        # Determine if the number is even or odd
        user_input = user_number % 2
        
        # Check if the number is even
        if user_input == 0:
            print(f'{user_name}, {user_number} is an even number')
        else:
            print(f'{user_name}, {user_number} is an odd number')
        
        # Compare the number to 10 and provide feedback
        if user_number > 10:
            print(' and it is greater than ten')
        elif user_number < 10:
            print(' and it is is less than ten')
        else:
            print(f'{user_name}, {user_number} is equal to ten')
        break  # Exit the loop if the number is processed
        
    except ValueError:
        # Handle invalid input (non-numeric input)
        print('This is an invalid input. Please enter a valid integer.')

# List of books for the next section
books_list = [
    "To Kill a Mockingbird", "1984", "Moby-Dick", "Pride and Prejudice", 
    "The Great Gatsby", "The Catcher in the Rye", "The Hobbit", 
    "Brave New World", "War and Peace", "Crime and Punishment"
]

# Prompt the user to continue
input("(Press Enter to continue...)")

# Ask the user to choose a book from the list and give a description


# Book class and search functionality
# Define the Book class
class Book:
    # Initialize a Book object with title, author, and year published
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    # Return a description of the book
    def description(self):
        return f"'{self.title}' by {self.author}, published in {self.year_published}"
        # Define the Book class with the required attributes and a method to return the description


# Instantiate two Book objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)

# Display the descriptions of the books
print(book1.description())
print(book2.description())


# List of Book objects
books = [
    Book("Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949),
    Book("The Woman", "Herman Melville", 1851),
    Book("Pride and Prejudice", "Jane Austen", 1813)
]

# Function to sort books by the year published
def sort_books_by_year(books):
    try:
        if not books:
            raise ValueError("The list of books is empty.")
        # Sort the books by year of publication
        return sorted(books, key=lambda book: book.year_published)
    except ValueError as e:
        print(f"Error: {e}")
        return []

# Sort the books by year published
sorted_books = sort_books_by_year(books)

# Display the sorted books using both for and while loops
print("\nBooks sorted by publication year (For loop):")
for book in sorted_books:
    print(book.description())

print("\nBooks sorted by publication year (While loop):")
i = 0
while i < len(sorted_books):
    print(sorted_books[i].description())
    i += 1

# Advanced Looping: Allow the user to search for a book by title
def find_book(book_name, books):
    # Search for the book by title
    for book in books:
        if book.title.lower() == book_name.lower():
            return book
    return None  # Return None if the book is not found

while True:
    # Ask the user to input the name of a book they want to search for
    print(f'{user_name}, enter the name of a book from the list below and I will give you a description: ')
    print(books_list)  # Show the list of books
    input("(Press Enter to continue...)")
    search_query = input("\nEnter the title of a book to search (or 'exit' to quit): ")

    if search_query.lower() == 'exit':
        print("Goodbye!")
        break

    # Find the book and display its description
    book = find_book(search_query, sorted_books)
    if book:
        print(book.description())  # Print the description of the found book
    else:
        print(f"Sorry, no book titled '{search_query}' was found. Please try again.")