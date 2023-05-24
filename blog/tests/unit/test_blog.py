from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        title, author = "My Blog", "Zac Sol"

        b = Blog(title, author)

        self.assertEqual(title, b.title)
        self.assertEqual(author, b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        title, author = "My Blog", "Zac Sol"
        b = Blog(title, author)

        self.assertEqual(f"{title} by {author} (0 posts)", b.__repr__())

    def test_json_no_posts(self):
        b = Blog("My Blog", "Zac Sol")

        expected = {
            "title": "My Blog",
            "author": "Zac Sol",
            "posts": []}

        self.assertDictEqual(expected, b.json())
