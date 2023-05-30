from blog import Blog

blogs = dict()  # blog_name : Blog object
MENU_PROMPT = 'Enter "c" to create a blog, \
                "l" to list blogs, \
                "r" to read, \
                "p" to create a post, \
                or "q" to quit.'
POST_TEMPLATE = """
--- {} ---

{}

"""


def menu():
    # Show the user the available blogs
    # Let the user select a choice
    # Do something with that choice
    # Eventually exit

    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    # print available blogs
    for key, blog in blogs.items():
        print(f"- {blog}")


def ask_create_blog():
    # ask for blog title and name, store in blogs dict
    title = input("Enter your blog title: ")
    author = input("Enter your name: ")
    blogs[title] = Blog(title, author)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def ask_read_blog():
    # ask for blog title and print posts
    title = input("Enter the blog title you want to read: ")

    print_posts(blogs[title])


def ask_create_post():
    #  ask for blog title, post title, post content, & create new post in the blog specified
    blog_title = input("Blog to append: ")
    post_title = input("New post title: ")
    content = input("New post content: ")

    blogs[blog_title].create_post(post_title, content)
