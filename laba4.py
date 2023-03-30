from abc import ABC, abstractmethod
from datetime import datetime
import logging
from typing import Dict


class Customs(ABC):
    def __init__(self):
        self.entries = []  # an empty list of entries that will contain information about people who cross the page

    @abstractmethod
    def cross_border(self, name: str, date: str):
        pass

    def analytics(self, start_date: str, end_date: str) -> int:
        count = 0
        for entry in self.entries:
            entry_date = datetime.strptime(entry['date'], "%Y-%m-%d")  #year-month-day
            # I convert the date string to a datetime
            # object, which we can compare to the start and end dates
            if start_date <= entry_date <= end_date:  # I check if the entry date is between the
                # start and end dates
                count += 1  # if the entry date is between the start and end dates, we increment the count
        return count


class LandCustoms(Customs):  # я создаю подкласс LandCustoms который в классе Customs
    def __init__(self):
        super().__init__()  # вызываю метод _init__ родительского класса, который инициализирует список записей
        self.type = 'land'
        self.logger = logging.getLogger('land_customs')  # передаю имя логера
        self.logger.setLevel(logging.INFO)  # register info lvl message
        fh = logging.FileHandler('land_customs.log')    # отправляет выходные данные журнала в файл
        fh.setLevel(logging.INFO)   #reg info lvl and high for FileHandler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh) #obrabotka logger

    def cross_border(self, name: str, date: str):
        entry = {'name': name, 'date': date, 'type': self.type}
        self.entries.append(entry)
        self.logger.info(f"New entry: {entry}")


class AirCustoms(Customs):
    def __init__(self):
        super().__init__()
        self.type = 'air'
        self.logger = logging.getLogger('air_customs')
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler('air_customs.log')
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def cross_border(self, name: str, date: str):
        entry: dict[str, str] = {'name': name, 'date': date, 'type': self.type}
        self.entries.append(entry)
        self.logger.info(f"New entry: {entry}")


if __name__ == "__main__":
    land_customs = LandCustoms()
    air_customs = AirCustoms()

    land_customs.cross_border('Amir', '2023-03-31')
    air_customs.cross_border('Anna', '2023-03-26')
    land_customs.cross_border('Kazbek', '2023-03-25')

    start_date = datetime.strptime('2023-03-25', '%Y-%m-%d')
    end_date = datetime.strptime('2023-03-31', '%Y-%m-%d')
    land_count = land_customs.analytics(start_date, end_date)
    air_count = air_customs.analytics(start_date, end_date)

    print(f"Land customs: {land_count} people crossed between {start_date} and {end_date}")
    print(f"Air customs: {air_count} people crossed between {start_date} and {end_date}")
