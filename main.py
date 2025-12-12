
def main():
        while True:
            choice = input('')
            if choice == '1':
                register_user()
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                login_user(username, password)
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")  