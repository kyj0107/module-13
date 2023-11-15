import unittest, datetime

def get_symbol():

    symbol = input("Enter a stocks symbol: ")
    if len(symbol) < 1 or len(symbol) > 7:
        raise Exception("Invalid length.")
    else:
        return symbol
    
def get_chart_type():

    chart_type = int(input("Enter a chart type. 1 for line, 2 for bar: "))
    if chart_type < 0 or chart_type > 2:
        raise Exception("Invalid number.")
    else:
        return chart_type
    
def get_time_series():

    time_series = int(input("Enter a time series. 1 for intraday, 2 for daily, 3 for weekly, or 4 for monthly: "))
    if time_series < 0 or time_series > 4:
        raise Exception("Invalid number.")
    else:
        return time_series
    
def get_start_date():

    start_date = input("Enter a date in YYYY-MM-DD format: ")

def get_end_date():

    end_date = input("Enter an end date in YYYY-MM-DD format: ")

class InputTest(unittest.TestCase):

    def test_get_symbol(self):

        pass

    def test_get_chart_type(self):

        pass

    def test_get_time_series(self):

        pass
    
    def test_start_date(self):

        start_date = get_start_date()
        is_start_date = bool(datetime.strptime(start_date, format))
        self.assertEqual(is_start_date, True)

    def test_end_date(self):

        end_date = get_end_date()
        is_end_date = bool(datetime.strptime(end_date, format))
        self.assertEqual(is_end_date, True)

if __name__ == "__main__": # God, I HATE this method of calling main()
    unittest.main()