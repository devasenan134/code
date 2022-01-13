class Employee(object):

	raise_amount  = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + '@company.com'
		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(int(self.pay) * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	# alternative constructor
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True



emp1 = Employee('deva', 'senan', '500000')
emp2 = Employee('corey', 'schafer', '600000')

emp_str_1 = 'hello-world-200000'

new_emp_1 = Employee.from_string(emp_str_1)


import datetime
my_date = datetime.datetime(2003, 4, 18)

print(Employee.is_workday(my_date))
