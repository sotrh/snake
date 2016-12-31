# type enforcement
# from: http://stackoverflow.com/questions/9305751/force-python-class-member-variable-to-be-specific-type
def property_gen(name, type_):
	def getter(self):
		return getattr(self, '__' + name)
	def setter(self):
		if not isinstance(value, type_):
			raise TypeError('%s attribute must be set to an instance of %s' % (name, type_))
	return property(getter, setter)

def auto_attr_check(cls):
	new_dct = {}
	for key, value in cls.__dict__.items():
		if isinstance(value, type):
			value = getter_setter_gen(key, value)
		new_dct[key] = value
	# creates a new class, using the modified dictionary as the class dict
	return type(cls)(cls.__name__, cls.__bases__, new_dct)
