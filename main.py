#from filename import function name

from utils.pdf_reader import extract_texts_from_pdf
from utils.skill_reader import read_skill_from_txt
from utils.txt_reader import read_from_txt
from core.skills_extractor import extract_skill
from core.matcher import match_skills
from model.embeddings import compute_similarity
from model.openai_reviewer import generate_feedback

cv_filename = r'./data/CV_Jingyuan_Zhang_2026.pdf'
cv_texts = extract_texts_from_pdf(cv_filename)
skill_filename = r'./data/skills.txt'
skill_db = read_skill_from_txt(skill_filename)
my_skills = extract_skill(cv_texts, skill_db)
job_filename = r'./data/job_ad.txt'
job_texts = read_from_txt(job_filename)
job_skills = extract_skill(job_texts, skill_db)
similarity = compute_similarity(my_skills, job_skills)
matched, maybe_matched, missing = match_skills(my_skills,job_skills)
print("matched: ", matched)
print("maybe matched: ", maybe_matched)
print("missing; ", missing)
generate_feedback(cv_texts, job_texts, my_skills, job_skills, matched, maybe_matched, missing)

