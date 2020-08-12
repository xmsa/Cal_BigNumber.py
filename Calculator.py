from Number import Num 

class Cal:
	def __init__(self, str1, str2):
		self.num1 = Num(str1)
		self.num2 = Num(str2)
		#print(self.Sum().Num2Str())
		#print(self.Minus().Num2Str())
		print(self.Mul().Num2Str())


	def Sum(self):
		sing1 = self.num1.GetSign()
		sing2 = self.num2.GetSign()
		int1 = self.num1.GetInt()
		int2 = self.num2.GetInt()
		float1 = self.num1.GetFloat()
		float2 = self.num2.GetFloat()

		num3 = Num()
		if sing1 == sing2 :
			num3.SetSign(sing1)

			s, c =  self.__Sum(float1, float2)
			num3.SetFloat(s)
			s, c = self.__Sum(int1, int2, c)
			num3.SetInt(s)

		elif sing1 and not(sing2) :
			self.num2.SetSign(True)
			
			num3 = self.Minus()

			tp=self.Greater(False)
			num3.SetSign(tp)
			self.num2.SetSign(False)

		elif not(sing1) and sing2 :

			self.num1.SetSign(True)
			num3 = self.Minus()
			self.num1.SetSign(False)
			tp=self.Greater(False)
			num3.SetSign(tp)
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
		sing1 = self.num1.GetSign()
		sing2 = self.num2.GetSign()
		int1 = self.num1.GetInt()
		int2 = self.num2.GetInt()
		float1 = self.num1.GetFloat()
		float2 = self.num2.GetFloat()
		f1 = len(float1) > len(float2)
		f2 = len(float2) > len(float1)

		if f1:
			float2 = self.__Sync(float2, len(float1))
		elif f2:
			float1 = self.__Sync(float1, len(float2))

		num3 = Num()
		#         -           +   or     +           -
		if (not(sing1) and sing2) or (sing1 and not(sing2)) :

			num3.SetSign(sing1)

			s, c =  self.__Sum(float1, float2)
			num3.SetFloat(s)
			
			s, c = self.__Sum(int1, int2, c)
			num3.SetInt(s)
		#      +         + 
		elif sing1 and sing2:
			if self.Greater():
				num3.SetSign(True)

				s, c =  self.__Minus(float1, float2)
				num3.SetFloat(s)
				
				s, c = self.__Minus(int1, int2, c)
				num3.SetInt(s)
			else:
				num3.SetSign(False)

				s, c =  self.__Minus(float2, float1)
				num3.SetFloat(s)
				
				s, c = self.__Minus(int2, int1, c)
				num3.SetInt(s)
		#           -             - 
		elif not(sing1) and not(sing2) :
			if self.Greater():
				num3.SetSign(True)

				s, c =  self.__Minus(float2, float1)
				num3.SetFloat(s)
				
				s, c = self.__Minus(int2, int1, c)
				num3.SetInt(s)
			else:
				num3.SetSign(False)

				s, c =  self.__Minus(float1, float2)
				num3.SetFloat(s)
				
				s, c = self.__Minus(int1, int2, c)
				num3.SetInt(s)
				pass
		return num3
	def __Minus(self, num1, num2, c=0 ):
		minus = list()

		for i in range(len(num2)):
			num1[i]-=c
			if num1[i] < num2[i]:
				num1[i]+=10
				if i+1!=len(num1):
					num1[i+1]-=1
				else:
					c=1
			minus.append(num1[i] - num2[i])

		for i in range(len(num2), len(num1)):
			num1[i]-=c
			if num1[i] < 0:
				num1[i]+=10
				if i+1!=len(num1):
					num1[i+1]-=1
				else:
					c=1
			minus.append(num1[i])
		
		return minus, c 

	def Greater(self, c = True):
		sing1 = self.num1.GetSign()
		sing2 = self.num2.GetSign()
		int1 = self.num1.GetInt()
		int2 = self.num2.GetInt()
		float1 = self.num1.GetFloat()
		float2 = self.num2.GetFloat()

		if c :
			s =self. CheckSing(sing1,sing2)
			if s != None:
				return s
			
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
			float2 = self.__Sync(float2, len(float1))
		elif f2:
			float1 = self.__Sync(float1, len(float2))

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

	def CheckSing(self,sing1,sing2):
		if sing1 and not(sing2):
			return True
		elif sing2 and not(sing1):
			return False
		return None

	def Mul(self):
		s=0
		num = list()
		__num1, l1 = self.num1.Merge()
		__num2, l2 = self.num2.Merge()
		for i in range(len(__num1)):
			for j in range(len(__num2)): 
				s = __num1[i] * __num2[j]
				if len(num)==i+j:
					num.append(0)
				num[i+j] += s
		for i in range(len(num)):
			if len(num) == i+1:
					num.append(0)
			num[i+1] += num[i] // 10
			num[i]=num[i] % 10
		s1 = self.num1.GetSign() or self.num2.GetSign()
		s2 = self.num1.GetSign() and self.num1.GetSign()
		if s1 == s2:
			s = True
		else:
			s = False
		
		n = Num()
		n.Split(num, l1+l2, s)
		return n

Cal("12.34","0.1")