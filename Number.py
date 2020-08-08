class Num:
	def __init__(self, _str = None):
		if _str != None:
			self.__int, self.__float , self.__sing = self.__Str2Num(_str)
		else:
			self.__int = [0]
			self.__float = [0]
			self.__sing = True	
		print(self.Num2Str())
	def __Str2Num(self, _str):
		__int = list()
		__float = list()
		__sing = True
		fl = False

		if ord(_str[0]) == 45:
			__sing = False

		for i in range(len(_str)):
			if 47 < ord(_str[i]) < 58:
				if fl:
					__float.insert(0, ord(_str[i]) - 48)
				else:
					__int.insert(0, ord(_str[i]) - 48)
			elif  ord(_str[i]) == 46:
				if not(fl):
					fl = True

		return self.__RemoveZero(__int, False) ,self.__RemoveZero(__float), __sing
	def __RemoveZero(self, lst, rtl = True):
		if rtl:	
			lst.reverse()
		
		while (len(lst)>1):
			tp = lst.pop()
			if tp != 0:
				lst.append(tp)
				break
		
		if rtl:	
			lst.reverse()
		
		return lst

	def Num2Str(self):
		if self.__sing:
			__str = ''
		else:
			__str = '-'
		i = len(self.__int) - 1
		if i==-1:
			__str += str(0)
			
		while i > -1:
			__str += str(self.__int[i])
			i -= 1
		if len(self.__float) != 0:
			__str += "."

		i = len(self.__float) - 1
		
		while i > -1:
			__str += str(self.__float[i])
			i -= 1
			
		return __str

	def SetInt(self, num):
		self.__int = num
	def SetFloat(self, num):
		self.__float = num
	def SetSign(self, num):
		self.__sing = num

	def GetInt(self):
		return self.__int 
	def GetFloat(self):
		return self.__float 
	def GetSign(self):
		return self.__sing 
