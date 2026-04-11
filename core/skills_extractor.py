SKILLS_DB = [
	'python', 'sql','machine learning',
	'django','flask','fastapi',
	'docker'
] #capitalized var name make it const var(but you can still change it, it's just for reading and differentiating) 

def extract_skill(text):
	found = []
	for skill in SKILLS_DB:
		if skill in text:
			found.append(skill)
	return list(set(found))