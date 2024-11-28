import sqlite3


conn = sqlite3.connect('asm.db')
cursor = conn.cursor()

username_to_delete = input("Enter the username to delete: ")


cursor.execute("SELECT * FROM admin_users WHERE username = ?", (username_to_delete,))
user = cursor.fetchone()

if user:
    
    cursor.execute("DELETE FROM admin_users WHERE username = ?", (username_to_delete,))
    conn.commit()
    print(f"User '{username_to_delete}' deleted successfully.")
else:
    print(f"Error: User '{username_to_delete}' does not exist.")

conn.close()
