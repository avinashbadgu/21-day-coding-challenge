#Day 6 Project: Explore Binary Search with Python and Tkinter! 
#🚀 Create a sorted list, enter a number, and find out if it's present

import tkinter as tk

def binary_search():
    try:
        num = int(entry_number.get())
        input_list = list(map(int, entry_list.get().split()))
        if sorted(input_list) != input_list:
            raise ValueError("List must be sorted.")
        
        first = 0
        last = len(input_list) - 1
        found = False
        
        while first <= last and not found:
            mid = (first + last) // 2
            if input_list[mid] == num:
                found = True
            else:
                if num < input_list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
    
        if found:
            result_label.config(text="Number found in the list")
        else:
            result_label.config(text="Number NOT found in the list")
            
    except ValueError as e:
        result_label.config(text=str(e))

def clear_results():
    result_label.config(text="")

# Create an instance of tkinter window
window = tk.Tk()
window.geometry("700x350")
window.title("Binary Search")

# GUI components
tk.Label(window, text="Let's perform Binary Search", font=('Calibri 15')).pack(pady=20)
tk.Label(window, text="Enter a Sorted List", font=('Calibri')).pack()
entry_list = tk.StringVar()
entry_number = tk.StringVar()
tk.Entry(window, textvariable=entry_list).pack()
tk.Label(window, text='Enter number you want to search').pack()
tk.Entry(window, textvariable=entry_number).pack()

# Result label
result_label = tk.Label(window, font=('Calibri'))
result_label.pack()

# Buttons
tk.Button(window, text="Search", command=binary_search).pack()
tk.Button(window, text="Clear Results", command=clear_results).pack()

# Main loop
window.mainloop()
