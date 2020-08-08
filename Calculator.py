from Number import Num 

class Cal:
	def __init__(self, str1, str2):
		self.num1 = Num(str1)
		self.num2 = Num(str2)
		print(self.Greater())
	def Sum(self):
		pass

	def Minus(self):
		pass

	def Mull(self):
		pass

	def Greater(self):
		sing1 = self.num1.GetSign()
		sing2 = self.num2.GetSign()
		int1 = self.num1.GetInt()
		int2 = self.num2.GetInt()
		float1 = self.num1.GetFloat()
		float2 = self.num2.GetFloat()

		if sing1 and not(sing2):
			return True
		elif sing2 and not(sing1):
			return False
		
		else:
			sing = sing1 and sing2
			f1 = len(int1) > len(int2)
			f2 = len(int2) > len(int1)

			if sing:
				if f1:
					return True
				if f2:
					return False
				i =  len(int1) - 1
				while i > -1:
					if int1[i] > int2[i]:
						return True
					elif int2[i] > int1[i]:
						return False
					i-=1
			else:
				if f1:
					return False
				if f2:
					return True
				i =  len(int1) - 1
				while i > -1:
					if int1[i] > int2[i]:
						return False
					elif int2[i] > int1[i]:
						return True
					i-=1
			
			f1 = len(float1) > len(float2)
			f2 = len(float2) > len(float1)

			if f1:
				self.__Sync(float2, len(float1))
			elif f2:
				self.__Sync(float1, len(float2))

			if sing:
				i =  len(float1) - 1
				while i > -1:
					if float1[i] > float2[i]:
						return True
					elif float2[i] > float1[i]:
						return False
					i-=1
			else:
				i =  len(float1) - 1
				while i > -1:
					if float1[i] > float2[i]:
						return False
					elif float2[i] > float1[i]:
						return True
					i-=1
		return True
	def __Sync(self, num, l):
		i = 0
		j = l - len(num)
		while i < j:
			num.insert(0, 0)
			i += 1
		return num


Cal("10","10.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001")