from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_post(self):
        b = Blog("My Blog", "Zac Sol")
        post_title, content = "Post title", "This is a post."
        b.create_post(post_title, content)

        self.assertEqual(1, len(b.posts))
        self.assertEqual(post_title, b.posts[0].title)
        self.assertEqual(content, b.posts[0].content)

    def test_json(self):
        b = Blog("My Blog", "Zac Sol")
        post_title, content = "Post title", "This is a post."
        b.create_post(post_title, content)

        expected = {
            "title": "My Blog",
            "author": "Zac Sol",
            "posts": [
                {"title": post_title,
                 "content": content}
            ]}

        self.assertDictEqual(expected, b.json())
