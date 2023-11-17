import unittest
from datetime import datetime

def get_symbol():

    symbol = input("Enter a stocks symbol: ")
    return symbol
    
def get_chart_type():

    chart_type = input("Enter a chart type. 1 for bar, 2 for line: ")
    return chart_type
    
def get_time_series():

    time_series = input("Enter a time series. 1 for intraday, 2 for daily, 3 for weekly, or 4 for monthly: ")
    return time_series
    
def get_start_date():

    start_date = input("Enter a start date in YYYY-MM-DD format: ")
    return start_date

def get_end_date():

    end_date = input("Enter an end date in YYYY-MM-DD format: ")
    return end_date

class InputTest(unittest.TestCase):

    def test_get_symbol(self):

        symbol = get_symbol()
        correct_length = True if len(symbol) > 0 and len(symbol) < 8 else False
        self.assertEqual(correct_length, True)
        contains_numbers = any(chr.isdigit() for chr in symbol)
        self.assertNotEqual(contains_numbers, True)

    def test_get_chart_type(self):

        chart_type = get_chart_type()
        is_number = chart_type.isdigit()
        if (is_number == True):
            correct_length = True if len(chart_type) == 1 and (int(chart_type) > 0 and int(chart_type) < 3) else False
            self.assertEqual(correct_length, True)

    def test_get_time_series(self):

        time_series = get_time_series()
        is_number = time_series.isdigit()
        if (is_number == True):
            correct_length = True if len(time_series) == 1 and (int(time_series) > 0 and int(time_series) < 5) else False
            self.assertEqual(correct_length, True)
    
    def test_start_date(self):

        start_date = get_start_date()
        is_start_date = bool(datetime.strptime(start_date, '%Y-%m-%d'))
        if (is_start_date == True):
            self.assertEqual(is_start_date, True)

    def test_end_date(self):

        end_date = get_end_date()
        is_end_date = bool(datetime.strptime(end_date, '%Y-%m-%d'))
        if (is_end_date == True):
            self.assertEqual(is_end_date, True)
        
if __name__ == "__main__": # God, I HATE this method of calling main()
    unittest.main()

#https://www.w3schools.com/python/python_conditions.asp I can't believe I had to relearn how to write single-line if-else statements
#https://www.geeksforgeeks.org/python-check-if-string-contains-any-number/# For checking if a string contains a number