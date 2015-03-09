class Account(object):
	counter = 0	
	def __init__(self,holder,number,balance,credit_line = 1500 ):
		Account.counter += 1
		self.Holder = holder
		self.Number = number
		self.Balance = balance
		self.Creditline = credit_line

	def transfer(self,target,amount):
		if( self.Balance - amount < self.Creditline ):
			return False
		else:
			self.Balance  -= amount
			target.Balance += amount
			return True

	def deposit(self,amount):
		self.Balance = amount

	def withdraw(self,amount):
		if( self.Balance - amount < self.Creditline ):
			print self.Balance
			return False
		else:
			self.Balance = -amount
			return True
	def balance(self):
		return self.Balance

	def __del__(self):
		Account.counter -= 1
		print "called"

x = Account("Kumar" ,101,1000,100000)
x2 = x
del x
del x2
