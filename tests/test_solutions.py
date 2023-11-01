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
        inputs = ["10", "10"]
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.is_square()
        expected = True
        assert (
            actual == expected
        ), f"Expected the is_square() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test equal length / height
        inputs = ["-10", "-10"]
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.is_square()
        expected = True
        assert (
            actual == expected
        ), f"Expected the is_square() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test inequal length / height
        inputs = ["10", "20"]
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.is_square()
        expected = False
        assert (
            actual == expected
        ), f"Expected the is_square() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test inequal length / height
        inputs = ["-10", "10"]
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.is_square()
        expected = False
        assert (
            actual == expected
        ), f"Expected the is_square() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

    def test_get_greatest(self, monkeypatch):
        """
        Check whether the function returns the greatest of the two input numbers.
        """
        # test equal numbers
        inputs = ["10", "10"]
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_greatest()
        expected = 10
        assert (
            actual == expected
        ), f"Expected the get_greatest() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test inequal numbers in ascending order
        inputs = ["11", "33"]
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_greatest()
        expected = 33
        assert (
            actual == expected
        ), f"Expected the get_greatest() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test inequal numbers in descending order
        inputs = ["852", "2"]
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_greatest()
        expected = 852
        assert (
            actual == expected
        ), f"Expected the get_greatest() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

    def test_get_bmi_category(self, monkeypatch):
        """
        Check whether the function returns the correct BMI statistical category, based on the input height/weight.
        """
        # test very severely underweight
        inputs = ["68", "78"]  # bmi 12
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_bmi_category().strip().capitalize()
        expected = "Very severely underweight".strip().capitalize()
        assert (
            actual == expected
        ), f"Expected the get_bmi_category() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test severely underweight
        inputs = ["67", "98"]  # bmi 15
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_bmi_category().strip().capitalize()
        expected = "Severely underweight".strip().capitalize()
        assert (
            actual == expected
        ), f"Expected the get_bmi_category() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test underweight
        inputs = ["70", "120"]  # bmi 17
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_bmi_category().strip().capitalize()
        expected = "Underweight".strip().capitalize()
        assert (
            actual == expected
        ), f"Expected the get_bmi_category() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test normal
        inputs = ["69", "160"]  # bmi 24
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_bmi_category().strip().capitalize()
        expected = "Normal".strip().capitalize()
        assert (
            actual == expected
        ), f"Expected the get_bmi_category() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test overweight
        inputs = ["73", "210"]  # bmi 28
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_bmi_category().strip().capitalize()
        expected = "Overweight".strip().capitalize()
        assert (
            actual == expected
        ), f"Expected the get_bmi_category() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test moderately obese
        inputs = ["67", "200"]  # bmi 31
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_bmi_category().strip().capitalize()
        expected = "Moderately obese".strip().capitalize()
        assert (
            actual == expected
        ), f"Expected the get_bmi_category() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test severely obese
        inputs = ["64", "220"]  # bmi 36
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_bmi_category().strip().capitalize()
        expected = "Severely obese".strip().capitalize()
        assert (
            actual == expected
        ), f"Expected the get_bmi_category() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

        # test very severely obese
        inputs = ["61", "220"]  # bmi 42
        mock_values = inputs.copy()
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))
        actual = solutions.get_bmi_category().strip().capitalize()
        expected = "Very severely obese".strip().capitalize()
        assert (
            actual == expected
        ), f"Expected the get_bmi_category() function to return {expected} when the user input the values, {mock_values}; instead, it returned {actual}."

    def test_get_discount(self, monkeypatch):
        """
        Check that a discount is applied to orders of 5,000 units or more.
        """

        inputs = [50, 222, 5000, 7012]
        mock_values = inputs.copy()
        expecteds = ["$250", "$1,110", "$20,000", "$28,048"]
        monkeypatch.setattr("builtins.input", lambda x: inputs.pop(0))

        for i, mock_data in enumerate(mock_values):
            expected = expecteds[i]

            actual = solutions.get_discount()
            assert (
                actual == expected
            ), f'Expected the get_discount() function to return {expected} when the user input the value, "{mock_data}"; instead, it returned {actual}.'

    def test_is_leap_year(self, monkeypatch):
        """
        Check that we can determine leap years correctly.
        """

        inputs = [
            1999,
            1652,
            1701,
            2000,
        ]  # regular non-leap, regular leap, century non-leap, century leap
        mock_values = inputs.copy()
        expecteds = [False, True, False, True]
        monkeypatch.setattr("solutions.get_year", lambda: inputs.pop(0))

        for i, mock_data in enumerate(mock_values):
            expected = expecteds[i]

            actual = solutions.is_leap_year()
            assert (
                actual == expected
            ), f"Expected the is_leap_year() function to return {expected} for the year {mock_data}; instead, it returned {actual}."
