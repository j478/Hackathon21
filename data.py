#define provider obj: name, how long provided, what they provide

class providers:
	string = db.Column(db.String(100))

	def __init__(self, string):
		self.string = string
		

#define 