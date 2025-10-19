import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    rating = rating_var.get()
    feedback = feedback_text.get("1.0", "end").strip()

    # Check all fields are filled
    if not name or not email or not rating or not feedback:
        messagebox.showwarning("Missing Info", "Please fill out all fields.")
        return

    # Ensure email ends with "@gmail.com"
    if not email.endswith("@gmail.com"):
        messagebox.showerror("Invalid Email", "Please enter a valid Gmail address (must end with @gmail.com).")
        return

    messagebox.showinfo("Feedback Submitted",
        f"Thank you for your feedback!\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Rating: {rating}\n"
        f"Feedback: {feedback}")

root = tk.Tk()
root.title("Feedback Form")
root.geometry("350x350")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Rating (1-5):").pack()
rating_var = tk.StringVar()
tk.OptionMenu(root, rating_var, "1", "2", "3", "4", "5").pack()

tk.Label(root, text="Feedback:").pack()
feedback_text = tk.Text(root, height=5, width=30)
feedback_text.pack()

tk.Button(root, text="Submit", command=submit_feedback).pack(pady=10)

root.mainloop()
