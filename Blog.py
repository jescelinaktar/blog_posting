
class Blog:
    def __init__(self, blog_id, title, content, author):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author

    # String representation of a blog
    def __str__(self):
        # Slices the content of the blog to the first 3 words followed by "..." if it is longer
        blog_content = " ".join(self.content.split(" ")[:3]) + "..." if len(self.content.split(" ")) > 3 else self.content
        # Returns a formatted string to make it clearer to read the blog details
        return f"Blog(blog_id={self.blog_id}, title='{self.title}', author='{self.author}', content='{blog_content}')"

    def __repr__(self):
        return self.__str__() # Returns a call to __str__