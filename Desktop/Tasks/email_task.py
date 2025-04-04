class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    
    def mark_as_read(self):
        self.has_been_read = True

# Initialize empty inbox list
inbox = []

def populate_inbox():
    # Create 3 sample emails and add them to the inbox
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", 
                  "Congratulations on joining HyperionDev! We're excited to have you.")
    email2 = Email("sender2@example.com", "Great work on the bootcamp!", 
                  "Your progress in the bootcamp has been outstanding. Keep it up!")
    email3 = Email("sender3@example.com", "Your excellent marks!", 
                  "You've achieved top marks in your recent assessments. Well done!")
    
    inbox.extend([email1, email2, email3])

def list_emails():
    print("\nInbox:")
    for index, email in enumerate(inbox):
        print(f"{index} {email.subject_line}")

def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"\nContent: {email.email_content}\n")
        email.mark_as_read()
        print(f"Email from {email.email_address} marked as read.\n")
    else:
        print("\nInvalid email index!\n")

# Populate the inbox with sample emails
populate_inbox()

while True:
    print("\nEmail Simulator Menu:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")
    
    user_choice = input("What would you like to do? (1/2/3): ")
    
    if user_choice == "1":
        list_emails()
        if inbox:  # Only proceed if there are emails in the inbox
            try:
                email_index = int(input("\nEnter the index of the email you want to read: "))
                read_email(email_index)
            except ValueError:
                print("\nPlease enter a valid number!\n")
    elif user_choice == "2":
        print("\nUnread Emails:")
        unread_count = 0
        for email in inbox:
            if not email.has_been_read:
                print(f"- {email.subject_line}")
                unread_count += 1
        if unread_count == 0:
            print("No unread emails.\n")
    
    elif user_choice == "3":
        print("\nQuitting application. Goodbye!")
        break
    
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.\n")