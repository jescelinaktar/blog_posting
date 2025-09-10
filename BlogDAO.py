import sqlite3
from Blog import Blog

# This class handles all the database operations for blogs, allowing the program to interact with the Blog table
class BlogDAO:
    def __init__(self):
        self.connection = sqlite3.connect('Blog.db')  # Connects to the database file and creates it if it doesn't exist
        self.cursor = self.connection.cursor()  # Creates the cursor object to run SQL commands
        # Creates the Blog table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Blog (
                blog_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                author TEXT
            )
        """)
        self.connection.commit()    # Commits the table to the database

    def __del__(self):
        self.connection.close()     # Closes the database connection

    # This function adds a new blog post to the database
    def add_blog(self, title, content, author):
        sql = "INSERT INTO Blog (title, content, author) VALUES (?, ?, ?)"  # SQL query to insert data, "?" acts as a placeholder for the parameters
        args = (title, content, author) # Tuple containing data
        self.cursor.execute(sql, args)  # Executes the query
        self.connection.commit()    # Commits it to the database

    # This function gets a single blog post by its id
    def get_blog(self, blog_id):
        sql = "SELECT * FROM Blog WHERE blog_id = ?"    # This query gets the blog post that matches the specified id
        args = (blog_id,)
        row = self.cursor.execute(sql, args).fetchone() # Fetches one result

        if row is None:
            return None     # Returns none if there was no matching blog

        return Blog(row[0], row[1], row[2], row[3])     # Returns a Blog object

    # This function gets all the blogs from the database
    def get_all_blogs(self):
        blogs = []      # Empty list to hold all the blogs
        rows = self.cursor.execute("SELECT * FROM Blog").fetchall()    # Fetches all the rows from the Blog table

        for row in rows:
            blogs.append(Blog(row[0], row[1], row[2], row[3]))  # Loops through each row and converts it to a Blog object

        return blogs    # Returns the list of blogs

    # This function updates an existing blog post using the blog id
    def update_blog(self, blog):
        sql = """
            UPDATE Blog
            SET title = ?, content = ?, author = ?
            WHERE blog_id = ?
        """
        args = (blog.title, blog.content, blog.author, blog.blog_id)
        self.cursor.execute(sql, args)
        self.connection.commit()

    # This function deletes a blog post based off the id
    def delete_blog(self, blog_id):
        sql = "DELETE FROM Blog WHERE blog_id = ?"
        args = (blog_id,)
        self.cursor.execute(sql, args)
        self.connection.commit()

