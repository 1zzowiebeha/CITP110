"""Algorithm workbench 5 from Chapter 8 of our textbook."""

import unittest


def is_https(url: str) -> bool:
    """Determine whether the passed url is https or not."""
    if url.startswith('https://'):
        return True
    else:
        return False


class TestStringMethods(unittest.TestCase):
    urls = [
        'https://www.google.com',
        'http://www.google.com',
        'www.python.org',
        'https://www.wordpress.org',
        'https://docs.djangoproject.com/en/',
    ]

    def test_is_https(self):
        for url in type(self).urls:
            self.assertTrue(is_https(url))


if __name__ == "__main__":
    # Run test suite:
    unittest.main()