import unittest
import main

# Using tests to try and improve our functions


class TestMain(unittest.TestCase):
    def setUp(self):
        """Can you be used to set up some code before each function"""
        print('About to test a function')

    def test_do_stuff(self):
        """HIIIIIIIIIIIIIIII"""
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'string'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    # def test_do_stuff5(self):
    #     test_param = 0
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 5)

    def test_game(self):

        result = main.run_guess(5, 5)
        self.assertTrue(result)

    def test_game2(self):
        result = main.run_guess(5, 1)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = main.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = main.run_guess(5, '11')
        self.assertFalse(result)

    def tearDown(self):
        """Tears down after each test"""
        print("Cleaning up - reset variables")


if __name__ == '__main__':
    unittest.main()
    #  run all of the tests in the file

# python3 -m unittest
# can add -v to be verbose
