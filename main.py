#from filename import function name
from utils.pdf_reader import extract_texts_from_pdf
from core.skills_extractor import extract_skill

filename = r'/Users/yuan/Desktop/ai_job_agent/data/CV_Jingyuan_Zhang_2026.pdf'
texts = extract_texts_from_pdf(filename)
skills = extract_skill(texts)
print(skills)