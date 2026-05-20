def read_from_txt(filename: str) -> str:
	try:
		file = open(filename)
	except Exception as error:
		print("Failed to open txt file:", error)
		return
	res = file.read()
	return res.lower()