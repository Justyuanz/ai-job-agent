import fitz

def extract_texts_from_pdf(filename: str):
	"""
	Open a PDF file, extract text from every page,
	combine it into one lowercase string, and return it.
	"""
	try:
		doc = fitz.open(filename)
		#inspect_pdf(doc)
	except Exception as error:
		print("Failed to open PDF:", error)
		return

	page_text = ''
	for page_index, page in enumerate(doc):
		page_text += page.get_text() + "\n"
	doc.close()
	return page_text.lower().strip()

# def inspect_pdf(doc: fitz.Document):

# 	print("doc type:")
# 	print(type(doc))

# 	print("doc length:")
# 	print(len(doc))

# 	first_page = doc[0]

# 	print("first_page type:")
# 	print(type(first_page))

	# print("dir(doc):")
	# print(dir(doc))