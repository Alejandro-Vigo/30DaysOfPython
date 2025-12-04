#Day 21: 30 Days of python programming

import math
class Statistics:
    def __init__(self, numbers):
        self.numbers=numbers
    def calculate_mean(self):
        return sum(self.numbers)/len(self.numbers)
    def calculate_median(self):
        sorted_list = sorted(self.numbers)
        mid = len(sorted_list) //2
        if len(sorted_list)%2 ==0:
         return (sorted_list[mid -1] + sorted_list[mid])/2
        return sorted_list[mid]
    def calculate_mode(self):
        frequency = {}
        for num in self.numbers:
            if num in frequency:
                frequency[num] +=1
            else: frequency[num] = 1
        max_count = max(frequency.values())
        mode = []
        for key, value in frequency.items():
            if value == max_count:
             mode.append(key)
        return mode
    def calculate_range(self):
        return max(self.numbers) - min(self.numbers)
    def calculate_variance(self):
        n = len(self.numbers)
        if n < 2:
            return None
        mean = sum(self.numbers)/n
        squared_diff = sum((x - mean) ** 2 for x in self.numbers)
        variance = squared_diff / (n - 1)
        return variance
    def calculate_std(self):
        variance = self.calculate_variance()
        std_deviation = math.sqrt(variance)
        return std_deviation
    def calculate_min_max(self):
        return min(self.numbers), max(self.numbers)
    def count(self):
        return len(self.numbers)
    def calculate_frequency(self):
        dicc_freq = {}
        for number in self.numbers:
            if number in dicc_freq:
                dicc_freq[number] +=1
            else: dicc_freq[number] = 1
        freq_list = sorted(dicc_freq.items(), key=lambda x: x[1], reverse=True)
        return freq_list

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
stats = Statistics(ages)
print(stats.calculate_mean())
print(stats.calculate_median())
print(stats.calculate_mode())
print(stats.calculate_range())
print(stats.calculate_variance())
print(stats.calculate_std())
print(stats.calculate_min_max())
print(stats.count())
print(stats.calculate_frequency())

#Exercise 2
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()
    def account_info(self):
        return f'{self.firstname} {self.lastname}'
    def total_income(self):
        return sum(amount for _, amount in self.incomes)
    def total_expense(self):
        return sum(amount for _, amount in self.expenses)
        '''total = 0
            for description, amount in self.expenses:
            total += amount
            return total'''
    def add_income(self, description, amount):
        self.incomes.add((description, amount))
    def add_expense(self, description, amount):
        self.expenses.add((description, amount))
    def account_balance(self):
        return self.total_income() - self.total_expense()
person = PersonAccount("Alex", "BD")
person.add_income("Salary", 50000)
person.add_expense("Rent", 1800)
print(person.account_info())
print(person.total_income()) 
print(person.total_expense())
print(person.account_balance())