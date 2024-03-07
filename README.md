# Lite-Text-Editor-using-python
![image](https://github.com/gitbiruk2010/Lite-Text-Editor-using-python/assets/103274295/070d146d-9854-47e6-80eb-71bf02a2aa72)


## Brief Description

This program is a lightweight python only text editor that runs in the command line interface (CLI). It allows the user to add text, delete the last character, and undo previous operations using a stack-based approach to manage changes.

## Features

- **Add Text**: Append characters to the text buffer.
- **Delete Text**: Remove the last character from the text buffer.
- **Undo**: Revert the most recent change, whether it's an addition or deletion of text.
- **Display**: Show the current state of the text after each operation.
- **Quit**: Exit the text editor.

## Usage

1. Start the program by running the Python script in your terminal.
2. Use the following commands:
   - To add text: `add <char>` where `<char>` is the character(s) you wish to add.
   - To delete the last character: `del`
   - To undo the last operation: `undo`
   - To quit the editor: `quit`

## How it Works

The editor uses a simple stack to track each text operation. Every addition or deletion pushes a new operation onto the stack, which can be popped off to undo the last change.

## System Requirements

- Python 3.6 or higher.

## Installation

No installation is required. Simply download the `TextEditor.py` file and run it in your Python environment.

## Contribution

Contributions are welcome. If you have any suggestions or improvements, please submit a pull request or open an issue.

