import unittest
import main


class TestsFlask(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()

    def test_sample(self):
        res = self.app.get("/")
        assert "Hello Flask World" in res.data.decode()


if __name__ == "__main__":
    unittest.main()
