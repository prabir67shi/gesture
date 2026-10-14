# ================================
# LETTER WRITING APPLICATION
# ================================

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# ---------- PART 1: the main window ----------
window = Tk()
window.title("Letter Writing Application")
window.geometry("600x500")

# Column 1 holds the editor, so column 1 is the one that grows
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)


# ---------- PART 2: open an existing letter ----------
def open_letter():
  """Open a saved letter for editing."""
  filepath = askopenfilename(
      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
  )

  if not filepath:  # The user pressed Cancel
    return

  txt_edit.delete(1.0, END)  # Clear first, or letters pile up

  with open(filepath, "r") as input_file:
    letter_text = input_file.read()
    txt_edit.insert(END, letter_text)

  window.title(f"Letter Writing Application - {filepath}")


# ---------- PART 3: save the letter under a new name ----------
def save_letter():
  """Save the letter as a text file."""
  filepath = asksaveasfilename(
      defaultextension=".txt",
      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
  )

  if not filepath:
    return

  with open(filepath, "w") as output_file:
    letter_text = txt_edit.get(1.0, END)
    output_file.write(letter_text)

  window.title(f"Letter Writing Application - {filepath}")


# ---------- PART 4: the widgets ----------
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)

# No parentheses — hand over the function, do not run it during setup
btn_open = Button(fr_buttons, text="Open Letter", command=open_letter)
btn_save = Button(fr_buttons, text="Save Letter As...", command=save_letter)


# ---------- PART 5: lay it out with grid ----------
# Inside the frame
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# Inside the window
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


# ---------- PART 6: start the program ----------
window.mainloop()