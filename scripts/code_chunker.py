''' 
NAME
    code_chunker.py

PURPOSE
    To split the content from the clipboard into manageable chunks and facilitate easy copying of these chunks.

DESCRIPTION
    This script reads text content from the clipboard, splits it into chunks of 2000 characters each, and provides a GUI to copy each chunk individually. 
    It is particularly useful for handling large blocks of text that need to be pasted in environments with character limits.

PROCESS
    1) The script reads the content passed as a command-line argument.
    2) It splits the content into chunks of 2000 characters each.
    3) A GUI is created with a status label and a canvas for scrollable content.
    4) Each chunk is presented in a separate card within the GUI, along with a button to copy the chunk to the clipboard.
    5) When a chunk is copied, a status message is displayed, which disappears after 3 seconds.

INPUT
    Text content from the clipboard, passed as a command-line argument.

OUTPUT
    The script outputs a GUI window with scrollable text chunks. 
    Each chunk can be copied to the clipboard with the click of a button. A status message confirms the action.

DEPENDENCIES
    - tkinter for creating the GUI elements
    - sys to read command-line arguments
    - pyperclip to handle copying text to the clipboard.
'''

import tkinter as tk
import sys, pyperclip

# Function to split clipboard content into manageable chunks
def get_clipboard_chunks():

    # Read the content passed as a command line argument 
    content = sys.argv[1]

    # Split content into chunks of 2000 characters each
    return [content[i:i+2000] for i in range(0, len(content), 2000)]


# Function to copy a chunk of text to the clipboard and display a status message
def copy_to_clipboard(chunk):
    pyperclip.copy(chunk)  # Copy the chunk to the clipboard
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(chunk)  # Append the chunk to the clipboard
    status_label.config(text="Chunk copied to clipboard!")  # Update status label

    # Schedule the status message to disappear after 3 seconds
    root.after(3000, lambda: status_label.config(text=""))


# Main application window
root = tk.Tk()
root.title("Code Chunker")  # Set the window title
root.geometry('+0+0')  # Position the window at the top-left corner of the screen


# Status label to display copy confirmation
status_label = tk.Label(root, text="")
status_label.pack()


# Calculate dynamic height for the canvas based on the number of chunks
dynamic_height = 220 * len(get_clipboard_chunks())
max_height = root.winfo_screenheight() - 100  # Maximum height for the canvas


# Create a canvas for scrollable content
canvas = tk.Canvas(
    root,
    height=dynamic_height if dynamic_height < max_height else max_height,
    width=400
)


# Scrollbar for the canvas
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)


# Frame to hold the content inside the canvas
frame = tk.Frame(canvas)


# Generate cards for each chunk with a copy button
for i, chunk in enumerate(get_clipboard_chunks()):
    card = tk.Frame(frame, borderwidth=2, relief="ridge", bg="white")
    card.pack(fill='both', expand=True, pady=5, padx=10)

    title = tk.Label(card, text=f"Chunk {i+1}", font=('Arial', 13, 'bold'))
    title.pack(side='top', fill='x', pady=5)

    snippet = tk.Label(card, text=chunk[:70] + '...', font=('Arial', 11), bg='white', wraplength=400)
    snippet.pack(side='top', fill='x', pady=5)

    copy_button = tk.Button(card, text="Copy", command=lambda c=chunk: copy_to_clipboard(c))
    copy_button.pack(side='bottom', fill='x', pady=5)


# Add the frame to the canvas and configure scrollbar
canvas.create_window(0, 0, anchor='nw', window=frame)
canvas.update_idletasks()


# Pack the canvas and scrollbar into the window
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')


# Start the Tkinter event loop
root.mainloop()