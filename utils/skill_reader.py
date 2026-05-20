def read_skill_from_txt(filename: str) -> list[str]:
	res = []
	try:
		file = open(filename)
	except Exception as error:
		print("Failed to open txt file:", error)
		return
	for line in file:
		res.append(line.lower().strip())
	return res