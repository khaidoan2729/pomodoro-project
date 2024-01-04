import tkinter as tk
'''
def button_clicked():
    user_input = entry.get()
    tbox = tk.Text()
    tbox.pack()

root = tk.Tk()
root.title("Destract")

label = tk.Label(root, text="How much time is allowed")
label.pack()

entry = tk.Entry(root)
entry.pack()
print((type)(entry))

button = tk.Button(root, text="Submit", command=button_clicked)
button.pack()

root.mainloop()

import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("Time's up!")

# Set the number of seconds for the timer
timer_duration = 10  # Change this to the desired duration
countdown_timer(timer_duration)

import tkinter as tk

def show_additional_text():
    additional_label.config(text="Additional text below the button")

root = tk.Tk()
root.title("Text Before and After Button")

# Create a label for text above the button
above_text_label = tk.Label(root, text="Text above the button")
above_text_label.pack()

# Create the button
button = tk.Button(root, text="Click me!", command=show_additional_text)
button.pack()

# Create a label for additional text below the button
additional_label = tk.Label(root, text="", fg="blue")
additional_label.pack()

root.mainloop()
'''
import tkinter as tk
import time

def update_label_text(a):
    global a
    new_text = str(a)  # Get text from the Entry widget
    a += 1
    label.config(text=new_text)  # Update the label text

root = tk.Tk()
root.title("Updating Label Text")
a = 0 
# Create an Entry widget to input new text
entry = tk.Entry(root)
entry.pack()

# Create a Label widget to display text
label = tk.Label(root, text="Initial Text")
label.pack()

update_label_text(a)
time.sleep(1)
root.mainloop()
