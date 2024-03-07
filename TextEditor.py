# Importing queue, time, random, and datetime modules
import queue
import time
import random
from datetime import datetime

# Define the TextOperation class to keep track of each operation
class TextOperation:
    def __init__(self, operation_type, character=None):
        # Initialize the operation type and the character involved
        self.operation_type = operation_type  # Possible values: 'add' or 'delete'
        self.character = character

# Define the TextEditor class to manage text editing
class TextEditor:
    def __init__(self):
        # Initialize the text editor with an empty text and an operations stack
        self.text = ""
        self.operations = []

    def add_text(self, character):
        # Add a character to the text and record the operation
        self.text += character
        self.operations.append(TextOperation('add', character))
        # Display the current text
        self.display()

    def delete_text(self):
        # Delete the last character from the text and record the operation
        if self.text:
            deleted_character = self.text[-1]
            self.text = self.text[:-1]
            self.operations.append(TextOperation('delete', deleted_character))
            # Display the current text
            self.display()

    def undo(self):
        # Undo the last operation performed on the text
        if self.operations:
            last_operation = self.operations.pop()
            if last_operation.operation_type == 'add':
                # Undo the add operation
                self.text = self.text[:-1]
            elif last_operation.operation_type == 'delete':
                # Undo the delete operation
                self.text += last_operation.character
            # Display the current text
            self.display()

    def display(self):
        # Display the current state of the text
        print(f"Current state of the text: \"{self.text}\"")

    def run(self):
        # Run the main loop for the text editor, processing user commands
        print("="*60)
        print("\t\t\tText Editor")
        print("="*60)
        print("\nCommands to choose: add <char>, del, undo, quit")
        while True:
            # Get user input for the command
            command = input("Enter command: ").strip()
            if command == 'exit':
                # Exit the editor
                print("Goodbye!")
                break
            elif command.startswith('add '):
                # Split the command to get the character(s) to add
                _, char = command.split(maxsplit=1)
                # Add the character(s) to the text
                self.add_text(char)
            elif command == 'del':
                # Delete the last character
                self.delete_text()
            elif command == 'undo':
                # Undo the last operation
                self.undo()
            else:
                # Inform the user of an unknown command
                print("Command Error. Please use: add <char>, del, undo, exit")

# Example usage: create an instance of TextEditor and run it
editor = TextEditor()
editor.run()
