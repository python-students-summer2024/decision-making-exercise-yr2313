import solutions

class Tests:

    def test_is_sweltering(self, monkeypatch):
        """
        Check whether the function returns True for temperatures above 90, and False for temperatures 90 and below.
        """

        # test with a super hot temperature
        monkeypatch.setattr("builtins.input", lambda x: '121')
        result = solutions.is_sweltering()
        assert result == True

        # test with the threshold temperature
        monkeypatch.setattr("builtins.input", lambda x: '90')
        result = solutions.is_sweltering()
        assert result == False

        # test with a cold temperature
        monkeypatch.setattr("builtins.input", lambda x: '52')
        result = solutions.is_sweltering()
        assert result == False

    def test_is_warm(self, capsys, monkeypatch):
        """
        Check whether the function returns True for temperatures between 75 and 87, inclusive, and False for other temperatures.
        """

        # test with a super hot temperature
        monkeypatch.setattr("builtins.input", lambda x: '121')
        result = solutions.is_warm()
        assert result == False

        # test with the threshold temperature
        monkeypatch.setattr("builtins.input", lambda x: '87')
        result = solutions.is_warm()
        assert result == True

        # test with the threshold temperature
        monkeypatch.setattr("builtins.input", lambda x: '75')
        result = solutions.is_warm()
        assert result == True

        # test with a cold temperature
        monkeypatch.setattr("builtins.input", lambda x: '52')
        result = solutions.is_warm()
        assert result == False

    def test_is_humid(self, capsys, monkeypatch):
        """
        Check whether the function returns True if the user answers "yes", and False otherwise.
        """

        # test with a 'yes'
        monkeypatch.setattr("builtins.input", lambda x: 'yes')
        result = solutions.is_humid()
        assert result == True

        # test with a 'no'
        monkeypatch.setattr("builtins.input", lambda x: 'no')
        result = solutions.is_humid()
        assert result == False

    def test_is_inclement(self, capsys, monkeypatch):
        """
        Check whether the function returns True if the user answers "rain", "snow", or "sleet"; and False otherwise.
        """

        # test with 'rain'
        monkeypatch.setattr("builtins.input", lambda x: 'rain')
        result = solutions.is_inclement()
        assert result == True

        # test with 'snow'
        monkeypatch.setattr("builtins.input", lambda x: 'snow')
        result = solutions.is_inclement()
        assert result == True

        # test with 'sleet'
        monkeypatch.setattr("builtins.input", lambda x: 'sleet')
        result = solutions.is_inclement()
        assert result == True

        # test with something else
        monkeypatch.setattr("builtins.input", lambda x: 'foo')
        result = solutions.is_inclement()
        assert result == False

        # test with something else
        monkeypatch.setattr("builtins.input", lambda x: 'bar')
        result = solutions.is_inclement()
        assert result == False

    def test_is_typical_new_york_summer(self, capsys, monkeypatch):
        """
        Check whether the function returns True if the is_sweltering() function returns True and the is_humid() function returns True;  False otherwise.
        """
        # test with a hot temperature and humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: True)
        monkeypatch.setattr("solutions.is_humid", lambda: True)
        result = solutions.is_typical_new_york_summer()
        assert result == True

        # test with a hot temperature but no humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: True)
        monkeypatch.setattr("solutions.is_humid", lambda: False)
        result = solutions.is_typical_new_york_summer()
        assert result == False

        # test with a cool temperature and humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: False)
        monkeypatch.setattr("solutions.is_humid", lambda: True)
        result = solutions.is_typical_new_york_summer()
        assert result == False

        # test with a cool temperature and no humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: False)
        monkeypatch.setattr("solutions.is_humid", lambda: False)
        result = solutions.is_typical_new_york_summer()
        assert result == False

    def test_is_cool_and_nice(self, capsys, monkeypatch):
        """
        Check whether the function returns True if the is_sweltering() function returns False and the is_humid() function returns False;  False otherwise.
        """
        # test with hot, humid, warm, and inclement
        monkeypatch.setattr("solutions.is_sweltering", lambda: True)
        monkeypatch.setattr("solutions.is_humid", lambda: True)
        monkeypatch.setattr("solutions.is_warm", lambda: True)
        monkeypatch.setattr("solutions.is_inclement", lambda: True)
        result = solutions.is_cool_and_nice()
        assert result == False

        # test with hot, humid, not warm, and not inclement
        monkeypatch.setattr("solutions.is_sweltering", lambda: True)
        monkeypatch.setattr("solutions.is_humid", lambda: False)
        monkeypatch.setattr("solutions.is_warm", lambda: False)
        monkeypatch.setattr("solutions.is_inclement", lambda: False)
        result = solutions.is_cool_and_nice()
        assert result == False

        # test with not hot, humid, not warm, and not inclement
        monkeypatch.setattr("solutions.is_sweltering", lambda: False)
        monkeypatch.setattr("solutions.is_humid", lambda: True)
        monkeypatch.setattr("solutions.is_warm", lambda: False)
        monkeypatch.setattr("solutions.is_inclement", lambda: False)
        result = solutions.is_cool_and_nice()
        assert result == False

        # test with not hot, not humid, warm, and not inclement
        monkeypatch.setattr("solutions.is_sweltering", lambda: False)
        monkeypatch.setattr("solutions.is_humid", lambda: False)
        monkeypatch.setattr("solutions.is_warm", lambda: True)
        monkeypatch.setattr("solutions.is_inclement", lambda: False)
        result = solutions.is_cool_and_nice()
        assert result == False

        # test with not hot, not humid, not warm, and inclement
        monkeypatch.setattr("solutions.is_sweltering", lambda: False)
        monkeypatch.setattr("solutions.is_humid", lambda: False)
        monkeypatch.setattr("solutions.is_warm", lambda: True)
        monkeypatch.setattr("solutions.is_inclement", lambda: True)
        result = solutions.is_cool_and_nice()
        assert result == False

        # test with not hot, not humid, not warm, and not inclement
        monkeypatch.setattr("solutions.is_sweltering", lambda: False)
        monkeypatch.setattr("solutions.is_humid", lambda: False)
        monkeypatch.setattr("solutions.is_warm", lambda: False)
        monkeypatch.setattr("solutions.is_inclement", lambda: False)
        result = solutions.is_cool_and_nice()
        assert result == True
