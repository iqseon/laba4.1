from abc import ABC, abstractmethod
from datetime import datetime
import logging


class Custom:
    pass


class Custom(ABC):
    def __init__(self):
        self.entries = [] # an empty list of entries that will contain information about ppl who cross the border

    @abstractmethod
    def cross_border(self, name: str, date: str):
        pass


    def analytics(self, start_date: str, end_date: str) -> int:
        count = 0
        for entry in self.entries:
            entry_date = datetime.strptime(entry['date'], "%Y-%m-%d")  # year-mounth-day
            # i convert the date string to a datatime
            # object which i can compare to the start and end dates
            if start_date <= entry_date <= end_date:  # i check if the entry date is btw the
                # start and end dates
                count += 1  # if the entry date is btw the start and end dates, we increment the count
        return count

class LandCustom(Custom):
        def __init__(self):
            super().__init__()
            self.type = 'land'
            self.logger = logging.getLogger('land_custom') #передаю имя логера
            self.logger.setLevel(logging.INFO) # register info lvl and high message
            fh = logging.FileHandler("land_custom.log") #sending output data in file
            fh.setLevel(logging.INFO) # reg info lvl and high for FH
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        def cross_border(self, name:str, date: str):
            """

            :param name:
            :param date:
            """
            entry = {'name': name, 'date': date, 'type': self.type}
            self.entries.append(entry)
            self.logger.info(f"New entry: {entry}")

        def get_entries_count(self, start_date, end_date):
            pass

class AirCustom(Custom):
        def __init__(self):
            super().__init__()
            self.type = 'air'
            self.logger = logging.getLogger('air_customs')
            self.logger.setLevel(logging.INFO)
            fh = logging.FileHandler('air_customs')
            fh.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        def cross_border(self, name:str, date: str):
            entry = {'name': name, 'date': date, 'type': self.type}
            self.entries.append(entry)
            self.logger.info(f"New entry {entry}")

        def analitycs(self, start_date, end_date):
            pass


if __name__ == '__main__':
    land_custom = LandCustom()
    air_custom = AirCustom()

    land_custom.cross_border('Ronaldo', '2023-03-27')
    air_custom.cross_border('Messi', '2023-03-26')
    land_custom.cross_border('Neymar', '2023-03-25')
    air_custom.cross_border('Mbappe', '2023-03-24')

    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    land_count = land_custom.analytics(start_date, end_date)
    air_count = air_custom.analytics(start_date, end_date)

    print(f"Land custom: {land_count} people crossed between {start_date} and {end_date}")
    print(f"Air suctom: {air_count} people crossed between {start_date} and {end_date}")



