"""
Do not run this file directly!  It won't work.
Run it using the Test panel in Visual Studio Code.
"""

import solutions

class Tests:

    def test_is_square(self, monkeypatch):
        """
        Check whether the function returns True when length and height are the same, False otherwise.
        """
        # test equal length / height
        input_values = ["10", "10"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.is_square()
        assert actual == True

        # test equal length / height
        input_values = ["-10", "-10"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.is_square()
        assert actual == True

        # test inequal length / height
        input_values = ["10", "20"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.is_square()
        assert actual == False

        # test inequal length / height
        input_values = ["-10", "10"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.is_square()
        assert actual == False

    def test_get_greatest(self, monkeypatch):
        """
        Check whether the function returns the greatest of the two input numbers.
        """
        # test equal numbers
        input_values = ["10", "10"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_greatest()
        assert actual == 10

        # test inequal numbers in ascending order
        input_values = ["11", "33"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_greatest()
        assert actual == 33
        
        # test inequal numbers in descending order
        input_values = ["852", "2"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_greatest()
        assert actual == 852
        
    def test_get_bmi_category(self, monkeypatch):
        """
        Check whether the function returns the correct BMI statistical category, based on the input height/weight.
        """
        # test very severely underweight
        input_values = ["68", "78"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_bmi_category().strip().lower()
        assert actual == "Very severely underweight".strip().lower()

        # test severely underweight
        input_values = ["67", "98"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_bmi_category().strip().lower()
        assert actual == "Severely underweight".strip().lower()

        # test underweight
        input_values = ["70", "120"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_bmi_category().strip().lower()
        assert actual == "Underweight".strip().lower()

        # test normal
        input_values = ["69", "160"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_bmi_category().strip().lower()
        assert actual == "Normal".strip().lower()

        # test overweight
        input_values = ["73", "210"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_bmi_category().strip().lower()
        assert actual == "Overweight".strip().lower()

        # test moderately obese
        input_values = ["67", "200"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_bmi_category().strip().lower()
        assert actual == "Moderately obese".strip().lower()

        # test severely obese
        input_values = ["64", "220"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_bmi_category().strip().lower()
        assert actual == "Severely obese".strip().lower()

        # test very severely obese
        input_values = ["61", "220"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = solutions.get_bmi_category().strip().lower()
        assert actual == "Very severely obese".strip().lower()

    def test_get_discount(self, monkeypatch):
        """
        Check that a discount is applied to orders of 500 units or more.
        """

        # test no discount for 10 units
        monkeypatch.setattr("builtins.input", lambda x: 50)
        expected = "$250"
        actual = solutions.get_discount()
        assert actual == expected

        # test no discount for 222 units
        monkeypatch.setattr("builtins.input", lambda x: 222)
        expected = '$1,110'
        actual = solutions.get_discount()
        assert actual == expected

        # test discount for 500 units
        monkeypatch.setattr("builtins.input", lambda x: 5000)
        expected = '$20,000'
        actual = solutions.get_discount()
        assert actual == expected

        # test discount for 712 units
        monkeypatch.setattr("builtins.input", lambda x: 7012)
        expected = '$28,048'
        actual = solutions.get_discount()
        assert actual == expected

    def test_is_leap_year(self, monkeypatch):
        """
        Check that we can determine leap years correctly.
        """

        # test regular non-leap yeaar
        monkeypatch.setattr("solutions.get_year", lambda: 1999)
        actual = solutions.is_leap_year()
        assert actual == False

        # test regular leap yeaar
        monkeypatch.setattr("solutions.get_year", lambda: 1652)
        actual = solutions.is_leap_year()
        assert actual == True

        # test century non-leap yeaar
        monkeypatch.setattr("solutions.get_year", lambda: 1700)
        actual = solutions.is_leap_year()
        assert actual == False

        # test century leap yeaar
        monkeypatch.setattr("solutions.get_year", lambda: 2000)
        actual = solutions.is_leap_year()
        assert actual == True
