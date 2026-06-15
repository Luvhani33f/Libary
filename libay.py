""""This module provides a function to connect to a SQLite database,"""
import sqlite3
import tkinter as tk
from tkinter import messagebox


db = sqlite3.connect("my_shelf_track.db")

# Get the cursor object
cursor = db.cursor()

# Create the author and ebookstore table if it does not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS author(
               author_id INTEGER PRIMARY KEY,
               name text,
               country text
               )
               ''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS ebookstore(
                   bookid INTEGER PRIMARY KEY,
                   booktitle text,
                   authorID INTEGER,
                   qty INTEGER,
                   FOREIGN KEY (authorID) REFERENCES author(author_id))
               ''')




def add_author():
    try:
    # Get number of authors from entry field
        
        author_records = []
            # Retrieve author details from entry fields
        author_id_input = entry_authorid.get().strip()
        name = entry_bookauthorname.get().strip()
        country = entry_bookauthorcountry.get().strip()

        # Validate inputs
        if not author_id_input or not name or not country:
            messagebox.showerror("Error", "All fields are required.")
            return

        if not author_id_input.isdigit():
            messagebox.showerror("Error", "Author ID must be a number.")
            return

        # Validate author ID
        author_id = int(author_id_input)
        if not (1000 <= author_id <= 9999):
            messagebox.showerror("Error", "Author ID must be 4 digits (1000-9999).")
            return

        author_records.append((author_id, name, country))
        
        cursor.executemany("INSERT INTO author(author_id, name, country) VALUES(?, ?, ?)", author_records)
        db.commit()
        
        messagebox.showinfo("Success", f"{len(author_records)} author record(s) saved successfully!")

    except ValueError:
        messagebox.showerror("Error", "Enter correct required values.")
             
        # Execute an INSERT INTO statemnet to the author table 
        # to enter author details
        # Commit the changes to save the data
        
        

def add_books():
    books_records = []
    try:  
    # number of books

        
        book_id_input = entry_bookid.get().strip()
        title = entry_booktitle.get().strip()
        author_id_input = entry_bookauthorid.get().strip()
        qty_input = entry_bookqty.get().strip()

        # Validate inputs
        if not book_id_input or not title or not author_id_input or not qty_input:
            messagebox.showerror("Error", "All fields are required.")
            return

        if not book_id_input.isdigit() or not author_id_input.isdigit() or not qty_input.isdigit():
            messagebox.showerror("Error", "Book ID, Author ID, and Quantity must be numbers.")
            return

        book_id = int(book_id_input)
        author_id = int(author_id_input)
        qty = int(qty_input)

        if qty < 0:
            messagebox.showerror("Error", "Quantity cannot be negative.")
            return

            # Check if book ID already exists
        cursor.execute("SELECT bookid FROM ebookstore WHERE bookid = ?", (book_id,))
        if cursor.fetchone():
                messagebox.showerror("Error", f"Book ID {book_id} already exists. Choose a different ID.")
                return

        books_records.append((book_id, title, author_id, qty))

    # Insert all records once
        cursor.executemany("INSERT INTO ebookstore(bookid, booktitle, authorID, qty) VALUES(?, ?, ?, ?)", books_records)
        db.commit()
        messagebox.showinfo("Success", f"{len(books_records)} book record(s) saved successfully!")

    except ValueError:
        messagebox.showerror("Error", "Enter correct required values.")

            # Update book title
def title_1():
    value = entry_bookinfo_title.get().strip()  
    if not value:
        messagebox.showerror("Error", "Please enter a valid book ID.")
        return
    if not value.isdigit():
        messagebox.showerror("Error", "Book ID must be a number.")
        return
    
    try:
        M = int(value)
    except ValueError:
        messagebox.showerror("Error", "Book ID must be a number.")
        return
    # Request user to enter new title
    new_title = entry_new_title.get().strip()
                     
                     # Check if input is empty
    if not new_title:
        messagebox.showerror("No new title entered")
                         
    else:
        # Execute an update statement for new title in table
        cursor.execute('''UPDATE ebookstore
                           SET booktitle = ?
                           WHERE bookid = ?
                           ''',(new_title, M))
                      # Fetch uupdated record
        cursor.execute("SELECT * FROM ebookstore WHERE bookid =?",(M,))
        db.commit()
        messagebox.showinfo("Updated record:",cursor.fetchone())
            # Update authorID
def author_id():
    book_id_input = entry_bookinfo_authorId.get().strip()
    if not book_id_input:
        messagebox.showerror("Error", "Please enter a Book ID.")
        return

    try:
        M = int(book_id_input)
    except ValueError:
        messagebox.showerror("Error", "Book ID must be a number.")
        return

    # Request user for new authorID
    new_authorId_input = entry_new_authorID.get().strip()
    if not new_authorId_input:
        messagebox.showerror("Error", "Please enter a new Author ID.")
        return

    try:
        new_authorId = int(new_authorId_input)
        # Validate authorId
        if 1000 <= new_authorId <= 9999:
            # Execute UPDATE statement
            cursor.execute(
                '''UPDATE ebookstore
                   SET authorID = ?
                   WHERE bookid = ?''',
                (new_authorId, M)
            )
            db.commit()

            # Fetch updated record
            cursor.execute("SELECT * FROM ebookstore WHERE bookid = ?", (M,))
            updated_record = cursor.fetchone()
            messagebox.showinfo("Success", f"Updated record: {updated_record}")
        else:
            messagebox.showerror("Error", "Author ID must be a 4-digit number.")
    except ValueError:
        messagebox.showerror("Error", "Author ID must be a number.")

            # Update quantity
def quantity_Num():
    M_input = entry_bookinfo_qty.get().strip()
    if not M_input:
        messagebox.showerror("Error", "Please enter a Book ID.")
        return
    if not M_input.isdigit():
        messagebox.showerror("Error", "Book ID must be a number.")
        return
    
    try:
        M = int(M_input)
    except ValueError:
        messagebox.showerror("Error", "Book ID must be a number.")
        return
    # request user to new quantity
    new_qty_input = entry_qty.get().strip()
    # Check if input is empty
    if not new_qty_input:
        messagebox.showerror("No new quantity entered")
        return
    else:
        
        try:
            # Convert input to integer
            new_qty = int(new_qty_input)
            
            # Execute and UPDATE statement for quantity
            cursor.execute('''UPDATE ebookstore
            SET qty = ?
            WHERE bookid = ?
            ''',(new_qty,M))
            # Fecth updated record to confirm change
            cursor.execute("SELECT * FROM ebookstore WHERE bookid =?",(M,) )
            db.commit()
            messagebox.showinfo("Updated record:",cursor.fetchone())
            
        except ValueError:
            messagebox.showerror("Quantity has to be a number")
            # Update author name and countr
def authour_an_name ():
    M_input = entry_bookinfo_authorId.get().strip()
    if not M_input:
        messagebox.showerror("Error", "Please enter a Book ID.")
        return
    if not M_input.isdigit():
        messagebox.showerror("Error", "Book ID must be a number.")
        return
    
    try:
        M = int(M_input)
    except ValueError:
        messagebox.showerror("Error", "Book ID must be a number.")
        return
    cursor.execute("SELECT * FROM ebookstore WHERE bookid = ?", (M,))
    book_id_info = cursor.fetchone()
    
    if not book_id_info:
        messagebox.showerror("Error", "No book found with the entered ID.")
        return
    
    # Execute a SELECT statement and join on ebookstore to author
    cursor.execute('''SELECT author.name,author.country FROM author
                                       JOIN ebookstore ON author.author_id = authorID
                                       WHERE bookid = ? 
                                       ''',(M,))
                # Fetch all matching records
    result = cursor.fetchall()
    for E in result:
                    name,country = E
                    messagebox.showinfo(f"Current record: author name:{name}, country:{country} ",)
                    
    new_name = entry_new_authorname.get().strip()
    new_country = entry_new_countryname.get().strip()
                
    if not new_name and not new_country:
                    messagebox.showerror("No new name or country entered")
                    return
    else:
                    # Execute a Update statement for author 
                    cursor.execute('''UPDATE author
                                       set name = ?, country = ?
                                       WHERE author_id = ?
                                       ''',(new_name,new_country, book_id_info[2]))
                    db.commit()
                # Execute a SELECT statement and JOIN ebookstore to author
    cursor.execute('''SELECT author.name,author.country FROM author
                                JOIN ebookstore ON author.author_id = authorID
                                WHERE bookid = ? 
                                       ''',(M,))
                # Fetch all matching records
    result = cursor.fetchall()
    for R in result:
                    name,country = R
                    messagebox.showinfo(f"Updated record: author name:{name},\
country:{country} ",)
                
            
                
def delete_book_info():
    # request user to enter book id comma-separated
    M = entry_delete_bookinfo.get()
    try:
      # Convert input string into list of integers 
      id_M_list = [int(i.strip()) for i in M.split(",")]
      # Validate all Id to be four digits
      if not all(1000<= i <= 9999 for i in id_M_list):
          messagebox.showerror("All mut be 4 digits")
      else:  
          valid_records = []
          for book_id in id_M_list:
            # Check if book exists  
            cursor.execute("SELECT * FROM ebookstore WHERE bookid =?",(book_id,))
            result =cursor.fetchone()
            if result:
              valid_records.append((book_id,))
            else:
                messagebox.showerror("Error",f"No book found with ID: {book_id}")
            
            # Delete only if valid record exist
            if valid_records:
               cursor.executemany("DELETE FROM ebookstore where bookid = ?",\
                   valid_records)   
               db.commit()
               messagebox.showinfo("Deleted", "Selected books deleted successfully")
            else:
              messagebox.showerror("Error", "No valid records to delete")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers only")
        
def search_database_info():
    # request user to enter 
    M = entry_search.get().strip()
    
    if not M:
        messagebox.showerror("Error", "Please enter a search term.")
        return
    
    # if input is digit, Excecute a SELECT statement for book ID
    if M.isdigit():
        cursor.execute('''SELECT * FROM ebookstore
                       WHERE bookid = ?''', (int(M),))
    else:
        # else it searches using partial match for title
        cursor.execute('''SELECT * FROM ebookstore
                       WHERE booktitle LIKE ?
                       ''', ('%'+M+'%',))
    # Fetche all matching records
    Record = cursor.fetchall()
    
    # if record found, display them else display no match found
    if Record:
        messagebox.showinfo("Search record:", "\n".join(str(r) for r in Record))
    else:
        messagebox.showinfo("No matching book found")
        
def view_details_of_all_books():
    try:
        #
        #cursor.execute('''
            #SELECT ebookstore.bookid, ebookstore.booktitle, ebookstore.qty,
               #    author.name, author.country
           # FROM ebookstore
            
           # JOIN author ON ebookstore.authorID = author.authorID
      #  ''')
        cursor.execute('''SELECT ebookstore.bookid, ebookstore.booktitle,
                       ebookstore.qty, author.name,
                       author.country FROM ebookstore
                       JOIN author ON ebookstore.authorID = author.author_id
''')
        result = cursor.fetchall()

        if not result:
            messagebox.showinfo("No Records", "No books found in the database.")
            return

        # Build a single string with all records
        details = ""
        for book_id, booktitle, qty, name, country in result:
            details += f"ID: {book_id}\nTitle: {booktitle}\nQuantity: {qty}\nAuthor: {name}\nCountry: {country}\n\n"

        # Show all in one popup
        messagebox.showinfo("All Book Details", details)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch records: {e}")

def importfiles_W():
    cursor.execute('''Insert into ebookstore(bookid, booktitle, qty, authorID) VALUES (?, ?, ?, ?)
                   ''')  
      
        
def main_menu():
    messagebox.showinfo("Exit","Exited select menu")
    db.commit()
    db.close()
    root.destroy()
    

def hide_all_frames():
    frame_menu.pack_forget()
    frame_addbook.pack_forget()
    frame_delete.pack_forget()
    frame_updatebook.pack_forget()
    frame_addauthor.pack_forget()
    frame_search.pack_forget()
    frame_updateauthorId.pack_forget()
    frame_updatetitle.pack_forget()
    frame_updateqty.pack_forget()
    frame_viewall.pack_forget()

def show_update():
    hide_all_frames()
    frame_updatebook.pack(pady=20)
def show_author_frame():
    hide_all_frames()
    frame_addauthor.pack(pady=20)
def show_add_book_frame():
    hide_all_frames()
    frame_addbook.pack(pady=20)
def show_deleted():
    hide_all_frames()
    frame_delete.pack(pady=20)
def show_search():
    hide_all_frames()
    frame_search.pack(pady=20)
def show_view_all():
    hide_all_frames()
    frame_viewall.pack(pady=20)
    
def back_to_menu(current_frame):
    current_frame.pack_forget()
    frame_menu.pack(pady=20)
def show_update_title():
    hide_all_frames()
    frame_updatetitle.pack(pady=20)
def show_update_authorId():
    hide_all_frames()
    frame_updateauthorId.pack(pady=20)
def show_update_qty():
    hide_all_frames()
    frame_updateqty.pack(pady=20)
def show_update_authorname():
    hide_all_frames()
    frame_updateauthorId.pack(pady=20)

# Execute the menu of the code

root = tk.Tk()
root.title("Bookstore")

frame_menu = tk.Frame(root, bg="#f0f4f7")
frame_menu.pack(pady=50)


tk.Label(frame_menu, text="Library Menu", font=("Segoe UI", 16, "bold"), 
         bg="#f0f4f7", 
         fg="#2c3e50").grid(row=0, column=0, columnspan=2, pady=20)


btn_book = tk.Button(frame_menu, text="📚 Book", width=20, 
                     command=show_add_book_frame, bg="#3498db", fg="white", 
                     font=("Segoe UI", 11, "bold"))
btn_book.grid(row=1, column=0, padx=10, pady=10)

btn_author = tk.Button(frame_menu, text="✍️ Authors", width=20, 
                       command=show_author_frame, bg="#2ecc71", fg="white", 
                       font=("Segoe UI", 11, "bold"))
btn_author.grid(row=1, column=1, padx=10, pady=10)


btn_Update = tk.Button(frame_menu, text="🔄 Update Book", width=20, 
                       command=show_update, bg="#f39c12", fg="white", 
                       font=("Segoe UI", 11, "bold"))
btn_Update.grid(row=2, column=0, padx=10, pady=10)

btn_Delete = tk.Button(frame_menu, text="🗑️ Delete Books", width=20, 
                       command=show_deleted, bg="#e74c3c", fg="white", 
                       font=("Segoe UI", 11, "bold"))
btn_Delete.grid(row=2, column=1, padx=10, pady=10)


btn_viewall = tk.Button(frame_menu, text="📖 View All Books", width=20, 
                        command=show_view_all, bg="#9b59b6", fg="white", 
                        font=("Segoe UI", 11, "bold"))
btn_viewall.grid(row=3, column=0, padx=10, pady=10)

btn_search = tk.Button(frame_menu, text="🔍 Search Books", width=20, 
                       command=show_search, bg="#1abc9c", fg="white", 
                       font=("Segoe UI", 11, "bold"))
btn_search.grid(row=3, column=1, padx=10, pady=10)


btn_exit = tk.Button(frame_menu, text="🚪 Exit", width=20, 
                     command=main_menu, bg="#34495e", fg="white", 
                     font=("Segoe UI", 11, "bold"))
btn_exit.grid(row=4, column=0, columnspan=2, pady=15)

btn_import = tk.Button(frame_menu, text="Import files",width=20,
                       command= importfiles_W, bg="#16a085", fg="white", font=("Segoe UI", 11, "bold"))

# Author Frame
frame_addauthor = tk.Frame(root, bg="#f0f4f7")

tk.Label(frame_addauthor, text="Author ID:", 
         font=("Segoe UI", 11),
         bg="#f0f4f7").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_authorid = tk.Entry(frame_addauthor, font=("Segoe UI", 11), width=25)
entry_authorid.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_addauthor, text="Author Name:", 
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_bookauthorname = tk.Entry(frame_addauthor, 
                                font=("Segoe UI", 11), width=25)
entry_bookauthorname.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_addauthor, text="Author Country:", 
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_bookauthorcountry = tk.Entry(frame_addauthor, 
                                   font=("Segoe UI", 11), width=25)
entry_bookauthorcountry.grid(row=3, column=1, padx=10, pady=5)

tk.Button(frame_addauthor, 
          text="➕ Add Authors", 
          command=add_author, 
          bg="#3498db", fg="white", 
          font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(frame_addauthor, 
          text="🧹 Clear Fields", 
          command=lambda: 
              [entry_authorid.delete(0, tk.END), 
               entry_bookauthorname.delete(0, tk.END), 
               entry_bookauthorcountry.delete(0, tk.END)], 
              bg="#f39c12", fg="white", 
              font=("Segoe UI", 11, "bold"), 
              width=20).grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(frame_addauthor, 
          text="🚪 Exit", 
          command=main_menu, bg="#e74c3c", fg="white", 
          font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=6, column=0, columnspan=2, pady=10)

btn_back_book = tk.Button(
    frame_addauthor,
    text="⬅ Back to Menu",
    command=lambda: back_to_menu(frame_addauthor),
    bg="#95a5a6", fg="white",
    font=("Segoe UI", 11, "bold"),
    width=20
)
btn_back_book.grid(row=8, column=0, columnspan=2, pady=15)

# Book Frame
frame_addbook = tk.Frame(root, bg="#f0f4f7")
tk.Label(frame_addbook,text="📚 Add New Book"
         ,font=("Segoe UI", 16, "bold"), bg="#f0f4f7", fg="#2c3e50").grid(
    row=0, column=0, columnspan=2, pady=20
)

tk.Label(frame_addbook, text="Book ID:", 
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_bookid = tk.Entry(frame_addbook, font=("Segoe UI", 11), width=25)
entry_bookid.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_addbook, text="Book Title:", 
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_booktitle = tk.Entry(frame_addbook, font=("Segoe UI", 11), width=25)
entry_booktitle.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_addbook, text="Author ID:", 
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_bookauthorid = tk.Entry(frame_addbook, font=("Segoe UI", 11), width=25)
entry_bookauthorid.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame_addbook, text="Quantity:", 
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_bookqty = tk.Entry(frame_addbook, font=("Segoe UI", 11), width=25)
entry_bookqty.grid(row=4, column=1, padx=10, pady=5)

# Add Book button
btn_addbook = tk.Button(
    frame_addbook,
    text="➕ Add Books",
    command=add_books,
    bg="#3498db", fg="white",
    font=("Segoe UI", 11, "bold"),
    width=20
)
btn_addbook.grid(row=5, column=0, columnspan=2, pady=10)

# Clear Fields button
btn_clear = tk.Button(
    frame_addbook,
    text="🧹 Clear Fields",
    command=lambda: [
        entry_bookid.delete(0, tk.END),
        entry_booktitle.delete(0, tk.END),
        entry_bookauthorid.delete(0, tk.END),
        entry_bookqty.delete(0, tk.END)
    ],
    bg="#f39c12", fg="white",
    font=("Segoe UI", 11, "bold"),
    width=20
)
btn_clear.grid(row=6, column=0, columnspan=2, pady=10)

btn_back = tk.Button(
    frame_addbook,
    text="⬅ Back to Menu",
    command=lambda: back_to_menu(frame_addbook),
    bg="#95a5a6", fg="white",
    font=("Segoe UI", 11, "bold"),
    width=20
)
btn_back.grid(row=8, column=0, columnspan=2, pady=15)

# Exit button
btn_exit = tk.Button(
    frame_addbook,
    text="❌ Exit",
    command=main_menu,
    bg="#e74c3c", fg="white",
    font=("Segoe UI", 11, "bold"),
    width=20
)
btn_exit.grid(row=7, column=0, columnspan=2, pady=10)


# add update book
# Update Book Frame
frame_updatebook = tk.Frame(root, bg="#f0f4f7")

# Title
tk.Label(frame_updatebook, text="📚 Update Book Details",
         font=("Segoe UI", 16, "bold"), bg="#f0f4f7", fg="#2c3e50").grid(
    row=0, column=0, columnspan=2, pady=10
)

# Book ID Entry


# Action Buttons
btn_title = tk.Button(frame_updatebook, text="📖 Update Title",
                      width=20, command=show_update_title,
                      bg="#3498db", fg="white",
                      font=("Segoe UI", 11, "bold"))
btn_title.grid(row=2, column=0, padx=10, pady=10)

btn_authorId = tk.Button(frame_updatebook, text="🆔 Update Author ID",
                         width=20, command=show_update_authorId,
                         bg="#2ecc71", fg="white",
                         font=("Segoe UI", 11, "bold"))
btn_authorId.grid(row=2, column=1, padx=10, pady=10)

btn_qty = tk.Button(frame_updatebook, text="📦 Update Quantity",
                    width=20, command=show_update_qty,
                    bg="#f39c12", fg="white",
                    font=("Segoe UI", 11, "bold"))
btn_qty.grid(row=3, column=0, padx=10, pady=10)

btn_author_name = tk.Button(frame_updatebook,text="✍️Update Author Name",
                            width=21, command=show_update_authorname,
                            bg="#9b59b6", fg="white",
                            font=("Segoe UI", 11, "bold"))
btn_author_name.grid(row=3, column=1, padx=10, pady=10)

btn_exitq = tk.Button(frame_updatebook, text="🚪 Back to Menu",
                      width=20, command=main_menu,
                      bg="#e74c3c", fg="white",
                      font=("Segoe UI", 11, "bold"))
btn_exitq.grid(row=4, column=0, columnspan=2, pady=15)

# Update Title Frame
frame_updatetitle = tk.Frame(root, bg="#f0f4f7")
tk.Label(frame_updatetitle, text="📖 Update Book Title",
         font=("Segoe UI", 16, "bold"), bg="#f0f4f7", fg="#2c3e50").grid(
    row=0, column=0, columnspan=2, pady=20
)
         
tk.Label(frame_updatetitle, text="Enter Book ID:",
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_bookinfo_title = tk.Entry(frame_updatetitle, 
                                font=("Segoe UI", 11), width=30)
entry_bookinfo_title.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_updatetitle, text="New Title:",
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_new_title = tk.Entry(frame_updatetitle, font=("Segoe UI", 11), width=30)
entry_new_title.grid(row=2, column=1, padx=10, pady=5)
tk.Button(frame_updatetitle, text="Update Title", command=title_1, 
          bg="#3498db", fg="white", font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(frame_updatetitle, text="⬅ Back to Menu", 
          command=lambda: back_to_menu(frame_updatetitle), 
          bg="#95a5a6", fg="white", font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=4, column=0, columnspan=2, pady=15)

# Update Author ID Frame
frame_updateauthorId = tk.Frame(root, bg="#f0f4f7")
tk.Label(frame_updateauthorId, text="✍️ Update Author Name and Country",
         font=("Segoe UI", 16, "bold"), bg="#f0f4f7", fg="#2c3e50").grid(
    row=0, column=0, columnspan=2, pady=20
)
tk.Label(frame_updateauthorId, text="Enter Book ID:",
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_bookinfo_authorId = tk.Entry(frame_updateauthorId, 
                                   font=("Segoe UI", 11), width=30)
entry_bookinfo_authorId.grid(row=1, column=1, padx=10, pady=5)  

tk.Label(frame_updateauthorId, text="New Author Name:",
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_new_authorname = tk.Entry(frame_updateauthorId, 
                                font=("Segoe UI", 11), width=30)
entry_new_authorname.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_updateauthorId, text="New Author Country:",
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_new_countryname = tk.Entry(frame_updateauthorId, 
                                 font=("Segoe UI", 11), width=30)
entry_new_countryname.grid(row=3, column=1, padx=10, pady=5)

tk.Button(frame_updateauthorId, text="Update Author Info", 
          command=authour_an_name, bg="#9b59b6", fg="white", 
          font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=4, column=0, columnspan=2, pady=10) 
tk.Button(frame_updateauthorId, 
          text="⬅ Back to Menu", 
          command=lambda: back_to_menu(frame_updateauthorId), bg="#95a5a6", 
          fg="white", font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=5, column=0, columnspan=2, pady=15)

# Update Quantity Frame
frame_updateqty = tk.Frame(root, bg="#f0f4f7")

tk.Label(frame_updateqty, text="📦 Update Book Quantity",
         font=("Segoe UI", 16, "bold"), bg="#f0f4f7", fg="#2c3e50").grid(
    row=0, column=0, columnspan=2, pady=20)
tk.Label(frame_updateqty, text="Enter Book ID:",
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_bookinfo_qty = tk.Entry(frame_updateqty, font=("Segoe UI", 11), width=30)
entry_bookinfo_qty.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_updateqty, text="New Quantity:",
         font=("Segoe UI", 11), 
         bg="#f0f4f7").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_qty = tk.Entry(frame_updateqty, font=("Segoe UI", 11), width=30)
entry_qty.grid(row=3, column=1, padx=10, pady=5)
tk.Button(frame_updateqty, text="Update Quantity", 
          command=quantity_Num, bg="#f39c12", 
          fg="white", font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=4, column=0, columnspan=2, pady=10) 
tk.Button(frame_updateqty, text="⬅ Back to Menu", 
          command=lambda: back_to_menu(frame_updateqty), 
          bg="#95a5a6", fg="white", font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=5, column=0, columnspan=2, pady=15)


# delete book frame
frame_delete = tk.Frame(root, bg="#f0f4f7")

tk.Label(frame_delete, text="Enter Book IDs (comma-separated):", 
         font=("Segoe UI", 12), 
         bg="#f0f4f7").grid(row=0, column=0, padx=5, pady=5)

entry_delete_bookinfo = tk.Entry(frame_delete, width=30)
entry_delete_bookinfo.grid(row=1, column=0, padx=5, pady=5)

btn_delete = tk.Button(frame_delete, text="🗑️ Delete Books", 
                       command=delete_book_info, bg="#e74c3c", fg="white", 
                       font=("Segoe UI", 11, "bold"), width=20)
btn_delete.grid(row=2, column=0, pady=15)
btn_back_delete = tk.Button(frame_delete, text="⬅ Back to Menu", 
                            command=lambda: back_to_menu(frame_delete), 
                            bg="#95a5a6", fg="white", 
                            font=("Segoe UI", 11, "bold"), width=20)
btn_back_delete.grid(row=3, column=0, pady=15)    

# Search book frame
frame_search = tk.Frame(root, bg="#f0f4f7")

tk.Label(frame_search, text="Search Books by ID or Title:",
         font=("Segoe UI", 12), 
         bg="#f0f4f7").grid(row=0, column=0, padx=5, pady=5)
entry_search = tk.Entry(frame_search, width=30)
entry_search.grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_search, text="🔍 Search", 
          command=search_database_info, bg="#1abc9c", fg="white", 
          font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=2, column=0, pady=15)
tk.Button(frame_search, text="⬅ Back to Menu", 
          command=lambda: back_to_menu(frame_search), bg="#95a5a6", 
          fg="white", font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=3, column=0, pady=15)
tk.Button(frame_search, text="🚪 Exit", command=main_menu, bg="#e74c3c", 
          fg="white", font=("Segoe UI", 11, "bold"), 
          width=20).grid(row=4, column=0, pady=15)

#viewall
frame_viewall = tk.Frame(root, bg="#f0f4f7")
tk.Label(frame_viewall, text="View All Books", font=("Segoe UI", 16, "bold"), 
         bg="#f0f4f7", fg="#2c3e50").grid(row=0, column=0, pady=10)
tk.Button(frame_viewall, text="📖 View All Books", width=20, 
          command=view_details_of_all_books, bg="#9b59b6", fg="white", 
          font=("Segoe UI", 11, "bold")).grid(row=1, column=0, padx=10, pady=10)
btn_back_viewall = tk.Button(frame_viewall, text="⬅ Back to Menu", 
                             command=lambda: back_to_menu(frame_viewall), 
                             bg="#95a5a6", fg="white", 
                             font=("Segoe UI", 11, "bold"), width=20)
btn_back_viewall.grid(row=2, column=0, padx=10, pady=15)
btn_viewall_exit = tk.Button(frame_viewall, text="🚪 Exit", command=main_menu, 
                             bg="#e74c3c", fg="white", 
                             font=("Segoe UI", 11, "bold"), width=20)
btn_viewall_exit.grid(row=3, column=0, padx=10, pady=15)

root.mainloop()