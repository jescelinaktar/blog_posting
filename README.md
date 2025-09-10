# Flask Application for Managing Blog Posts

### Project Description:
This is a simple Blog Application built using Flask and SQLite3. The application allows users to create, view, update, and delete blog posts. It follows a DAO (Data Access Object) pattern to handle all database interactions.

### Set up Instructions:

- Download the zip file of the flask app from Canvas
- Extract the zip file and open with Pycharm
- Once open, there should be a template directory with the following files:
  - base.html
  - index.html
  - create_blog.html
  - edit_blog.html
  - view_details.html
  - about.html
  
- There should also be a directory called static, 
- Three python files called: 
  - app.py
  - Blog.py
  - BlogDAO.py
- A database called Blog.db should be there too, but if it does not exist it will be created automatically the first time the app runs

- When you click the run button, this link: http://127.0.0.1:5000 will show on the terminal, and you can click on it to direct you to the application

- From here you can see all the blog posts, individually select one and view the details, edit or delete it, add a new blog post or read the “About” section

### Design:

- This application uses Flask as the backend and HTML, JavaScript, CSS in the frontend
- It uses a SQLite3 database to store the blog posts
- The layout is designed to be responsive and user-friendly, with easy navigation between pages

### References:
- Nyakundi, H. (2021). How to Write a Good README File for Your GitHub Project. [online] freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/.
‌
- newdeveloper (2022). Jinja2 truncate string variable not working. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/71933033/jinja2-truncate-string-variable-not-working.
‌
- Muller, D. (2020). How To Use the sqlite3 Module in Python 3. [online] DigitalOcean. Available at: https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3.
‌



