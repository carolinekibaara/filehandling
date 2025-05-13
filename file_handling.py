# File Read & Write Challenge 🖋️
# Read content from input.txt and write to output.txt after modifying it

try:
    with open("input.txt", "r") as infile:
        content = infile.read()
        print("Content of input.txt:")
        print(content)
except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Modify the content (e.g., converting to uppercase)
modified_content = content.upper()

# Write modified content to output.txt
try:
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)
        print("Modified content written to 'output.txt'.")
except Exception as e:
    print(f"An error occurred while writing to 'output.txt': {e}")

# Error Handling Lab 🧪
# Ask the user for a filename and handle errors

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(f"Content of {filename}:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")
