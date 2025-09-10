from flask import Flask, render_template, request, redirect, url_for
from BlogDAO import BlogDAO

app = Flask(__name__)   # Initialise Flask app
app.secret_key = "your secret key"

# Route that displays all the blogs - essentially the homepage
@app.route('/', methods = ['GET'])
def index():
    blog_dao = BlogDAO()    # Creating an instance of BlogDAO
    blogs = blog_dao.get_all_blogs()    # Fetch all blogs from the database
    return render_template('index.html', blogs=blogs)     # Render the homepage with the blogs

# Route for creating a new blog post
@app.route('/create_blog', methods = ['GET', 'POST'])
def create_blog():
    blog_dao = BlogDAO()
    if request.method == 'POST': # If request is POST, this part of the code runs
        # The POST data is extracted into variables
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')

        # Validation to make sure there are no empty fields
        if not title or not content or not author:
            return render_template(
                'create_blog.html',
                error="You need to enter all the fields",
                fields={"title": title, "content": content, "author": author}
            )

        # This checks if the title already exists
        all_blogs = blog_dao.get_all_blogs()
        if title.lower() in [blog.title.lower() for blog in all_blogs]:
            return render_template(
                'create_blog.html',
                error="Another blog has that title",
                fields={"content": content, "author": author}
            )

        blog_dao.add_blog(title, content, author)   # Adds the new blog to the database

        return redirect(url_for('index'))   # Redirects to the homepage after the blog post is created

    # If request is GET, this gets executed instead
    return render_template('create_blog.html', fields={})

# Route for the about page
@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

# Route for editing blog posts
@app.route('/edit_blog/<int:blog_id>', methods = ['GET', 'POST'])
def edit_blog(blog_id):     # This function allows the user to edit a blog post
    blog_dao = BlogDAO()
    blog = blog_dao.get_blog(blog_id)

    if not blog:
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')

        if not title or not content or not author:
            return render_template(
                'edit_blog.html',
                error="You need to enter all the fields",
                blog=blog
            )

        all_blogs = blog_dao.get_all_blogs()
        if title.lower() in [blog.title.lower() for blog in all_blogs if blog.blog_id != blog_id]:
            return render_template(
                'edit_blog.html',
                error="Another blog has that title",
                blog=blog
            )

        blog.title = title
        blog.content = content
        blog.author = author
        blog_dao.update_blog(blog)

        return redirect(url_for('view_details', blog_id=blog_id))
    return render_template('edit_blog.html', blog=blog)

# This route is for deleting a blog post
@app.route('/delete_blog/<int:blog_id>', methods = ['POST'])
def delete_blog(blog_id):
    blog_dao = BlogDAO()
    blog = blog_dao.get_blog(blog_id)
    if blog:
        blog_dao.delete_blog(blog_id)
    else:
        # Redirects to index and give 404 (not found) if the user tries to delete a Blog that doesn't exist
        return redirect(url_for('index')), 404
    return redirect(url_for('index'))

# Route for showing individual blog posts
@app.route('/view_details/<int:blog_id>', methods = ['GET'])
def view_details(blog_id):
    blog_dao = BlogDAO()
    blog = blog_dao.get_blog(blog_id)
    return render_template('view_details.html', blog=blog)

if __name__ == '__main__':
    app.run()

