def process_file_with_error_handling():
    """
    Prompts the user for a filename, reads its content, converts it to uppercase,
    and writes the modified content to a new file named 'modified_output.txt'.
    Includes error handling for file-related issues.
    """
    input_filename = input("Enter the name of the file to read: ")
    output_filename = "modified_output.txt"

    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  # Modify the content (e.g., convert to uppercase)

        # Attempt to write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File '{input_filename}' successfully read and modified.")
        print(f"Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        print("Please ensure the filename is correct and the file exists in the current directory.")
    except IOError as e:
        print(f"Error: An I/O error occurred while processing the file: {e}")
        print("This might be due to permission issues or other file-related problems.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the function
process_file_with_error_handling()