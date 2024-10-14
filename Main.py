from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Function to create the homepage window
def create_homepage():
    global root
    root = customtkinter.CTk()
    root.title('Home Page')
    root.iconbitmap('/Users/jaiktom/Documents/Budget Tracker_/images/Budget.ico')
    root.geometry('400x300')
    
    title_label = customtkinter.CTkLabel(root, text="Welcome to Budgeted", font=("Arial", 30))
    title_label.pack(pady=30)
    
    login_button = customtkinter.CTkButton(root, text="Log In", command=open_login_window, corner_radius=10)
    login_button.pack(pady=10)
    
    signup_button = customtkinter.CTkButton(root, text="Sign Up", command=open_signup_window, corner_radius=10)
    signup_button.pack(pady=10)
    
    root.mainloop()

# Function to open the login window
def open_login_window():
    root.destroy()
    create_login_window()

# Function to open the signup window
def open_signup_window():
    root.destroy()
    create_signup_window()

# Function to go back to the homepage from login or signup
def go_back_to_homepage():
    login_window.destroy() if 'login_window' in globals() else signup_window.destroy()
    create_homepage()

# Function to create the login window
def create_login_window():
    global login_window
    login_window = customtkinter.CTk()
    login_window.title('Login Page')
    login_window.iconbitmap('/Users/jaiktom/Documents/Budget Tracker_/images/Budget.ico')
    login_window.geometry('400x300')

    # Function to handle login button click
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username == "user" and password == "password":
            message_label.configure(text="Login Successful!", text_color="green")
        else:
            message_label.configure(text="Invalid username or password.", text_color="red")

    title_label = customtkinter.CTkLabel(login_window, text="Login to Budgeted", font=("Arial", 30))
    title_label.pack(pady=10)
    
    frame = customtkinter.CTkFrame(login_window)
    frame.pack(pady=10)

    # Username Label and Entry
    username_label = customtkinter.CTkLabel(frame, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    username_entry = customtkinter.CTkEntry(frame, placeholder_text="Enter your username")
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    # Password Label and Entry
    password_label = customtkinter.CTkLabel(frame, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    password_entry = customtkinter.CTkEntry(frame, placeholder_text="Enter your password", show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Login Button
    login_button = customtkinter.CTkButton(frame, text="Login", command=login, corner_radius=10)
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Back Button to return to homepage
    back_button = customtkinter.CTkButton(login_window, text="Back", command=go_back_to_homepage, corner_radius=10)
    back_button.pack(pady=10)

    # Message Label for feedback
    message_label = customtkinter.CTkLabel(login_window, text="")
    message_label.pack(pady=10)

    login_window.mainloop()

# Function to create the signup window
def create_signup_window():
    global signup_window
    signup_window = customtkinter.CTk()
    signup_window.title('Sign Up Page')
    signup_window.iconbitmap('/Users/jaiktom/Documents/Budget Tracker_/images/Budget.ico')
    signup_window.geometry('400x300')

    title_label = customtkinter.CTkLabel(signup_window, text="Sign Up for Budgeted", font=("Arial", 30))
    title_label.pack(pady=10)
    
    frame = customtkinter.CTkFrame(signup_window)
    frame.pack(pady=10)

    # Username Label and Entry
    username_label = customtkinter.CTkLabel(frame, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    username_entry = customtkinter.CTkEntry(frame, placeholder_text="Choose a username")
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    # Password Label and Entry
    password_label = customtkinter.CTkLabel(frame, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    password_entry = customtkinter.CTkEntry(frame, placeholder_text="Choose a password", show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Sign Up Button
    signup_button = customtkinter.CTkButton(frame, text="Sign Up", corner_radius=10)
    signup_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Back Button to return to homepage
    back_button = customtkinter.CTkButton(signup_window, text="Back", command=go_back_to_homepage, corner_radius=10)
    back_button.pack(pady=10)

    signup_window.mainloop()

# Start the application with the homepage
create_homepage()
