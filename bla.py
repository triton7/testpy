'''
>>> class X(XDictAttr):
...     def get_foo(self):
...         return 5
...     def get_bar(self):
...         return 12


>>> x = X({'one': 1, 'two': 2, 'three': 3})
>>> x
{'one': 1, 'three': 3, 'two': 2}
>>> x['one']
1
>>> x.three
3
>>> x.bar
12
>>> x['foo']
5
>>> x.get('foo', 'missing')
5
>>> x.get('bzz', 'missing')
'missing'
'''
class XDictAttr(dict):
	def __getattr__(self, attr):
		try:
			if 'get_'+attr in self.__class__.__dict__:
				return self.__class__.__dict__['get_'+attr](self)
			return self[attr]
		except KeyError:
			raise AttributeError





if __name__ == "__main__":
    import doctest
    doctest.testmod()
