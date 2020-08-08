from Number import Num 

class Cal:
	def __init__(self, str1, str2):
		self.num1 = Num(str1)
		self.num2 = Num(str2)
		print(self.Sum().Num2Str())

	def Sum(self):
		sing1 = self.num1.GetSign()
		sing2 = self.num2.GetSign()
		int1 = self.num1.GetInt()
		int2 = self.num2.GetInt()
		float1 = self.num1.GetFloat()
		float2 = self.num2.GetFloat()

		if sing1 == sing2 or not(sing1==sing2):
			num3 = Num()
			num3.SetSign(sing1)

			s, c =  self.__Sum(float1, float2)
			num3.SetFloat(s)
			
			s, c = self.__Sum(int1, int2, c)
			num3.SetInt(s)
		else:
			pass

		return num3
		
	def __Sum(self, num1, num2, c=0 ):
		sum = list()

		for i in range(len(num2)):
			s = num1[i] + num2[i] + c
			c = s // 10
			sum.append(s % 10)

		for i in range(len(num2), len(num1)):
			s = num1[i] + c
			c = s // 10
			sum.append(s % 10)
		
		return sum, c

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


Cal("10.9","10.1")