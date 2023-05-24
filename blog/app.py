blogs = dict()  # blog_name : Blog object


def menu():
    # Show the user the available blogs
    #  Let the user name a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()


def print_blogs():
    # print available blogs
    for key, blog in blogs.items():
        print(f"- {blog}")
