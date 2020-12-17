class MainHandler():
	def checkQuery(query):
		if(query[:4] == "qry "):
			return "query is : " + query[4:]
		else:
			return "i don't understand the query :/"