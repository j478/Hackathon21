#define provider obj: name, how long provided, what they provide

class providers(db.Model):
	string = db.Column(db.String(100))

	def __init__(self, string):
        self.string = string"""

		

#define 