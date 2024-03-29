try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Another line with some text and numbers: 56789\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appended line 1.\n")
        file.write("Appended line 2.\n")
        file.write("Appended line 3.\n")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied to access the file.")

finally:
    print("File handling completed.")
