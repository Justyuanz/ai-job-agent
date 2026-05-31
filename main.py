#from filename import function name

from utils.pdf_reader import extract_texts_from_pdf
from utils.skill_reader import read_skill_from_txt
from utils.txt_reader import read_from_txt

from core.gmail_api import get_linkedin_job_alert_emails
from core.skills_extractor import extract_skill
from core.matcher import match_skills

from model.joblead_extractor import choose_the_best_job
#from core.esco_api import search_esco_skills
#from model.embeddings import compute_similarity
#from model.openai_reviewer import generate_feedback


def load_inputs():
	cv_filename = r'./data/CV.pdf'
	skill_filename = r'./data/skills.txt'
	job_filename = r'./data/job_ad.txt'

	cv_texts = extract_texts_from_pdf(cv_filename)
	skill_db = read_skill_from_txt(skill_filename)
	job_texts = read_from_txt(job_filename)
	return cv_texts, skill_db, job_texts

def analyze_job(cv_texts, skill_db, job_texts):
	"""
	first read job ad, extract from skill_db(not all the skills would be extracted here)
	then query esco api for potential skill to expand skill_db
	"""
	my_skills = extract_skill(cv_texts, skill_db)
	job_skills = extract_skill(job_texts, skill_db)
	matched, maybe_matched, missing = match_skills(my_skills,job_skills)
	return my_skills, job_skills, matched, maybe_matched, missing

def print_results(my_skills, job_skills, matched, maybe_matched, missing):
	print("\n=== CV SKILLS ===")
	print(my_skills)
	print("Count:", len(my_skills))

	print("\n=== JOB SKILLS ===")
	print(job_skills)
	print("Count:", len(job_skills))

	print("\n=== MATCHED ===")
	print(matched)
	print("Count:", len(matched))

	print("\n=== MAYBE MATCHED ===")
	print(maybe_matched)
	print("Count:", len(maybe_matched))

	print("\n=== MISSING ===")
	print(missing)
	print("Count:", len(missing))


def main():
	emails = get_linkedin_job_alert_emails()
	cv_texts, skill_db, job_texts = load_inputs()
	choose_the_best_job(cv_texts, emails)
	my_skills, job_skills, matched, maybe_matched, missing = analyze_job(cv_texts, skill_db, job_texts)

if __name__ == "__main__":
	main()
