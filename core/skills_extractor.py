def normalize_text(text: str) -> str:
	
	for char in ",.;:!?()[]{}\"'\n\t":
		text = text.replace(char, " ")

	text = " " + " ".join(text.split()) + " "

	return text

def extract_skill(text: str, skills: list) -> list[str]:
	found = [] #create an empty list(flexible array)
	padded_text = normalize_text(text)

	for skill in skills: #in checks whether something exists
		padded_skill= normalize_text(skill)
		if padded_skill in padded_text:
			found.append(skill)

	return list(set(found)) #set removes duplicate