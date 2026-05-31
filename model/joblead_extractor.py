import json
from datetime import datetime

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

CURRENT_LEADS_FILENAME = "data/current_leads.json"

def current_timestamp() -> str:
	return datetime.now().isoformat(timespec="seconds")

def load_prompt_template(filename: str) -> str:
	try:
		file = open(filename, "r")
	except Exception as error:
		print("Failed to open prompt file:", error)
		return ""
	return file.read()

def write_jobleads_to_file(selected_jobs: str) -> None:
	try:
		lead_data = json.loads(selected_jobs)
	except json.JSONDecodeError:
		lead_data = {
			"status": "waiting_for_full_job_ad",
			"job_ad_ready": False,
			"raw_selection": selected_jobs,
		}
	else:
		lead_data["status"] = "waiting_for_full_job_ad"
		lead_data["job_ad_ready"] = False
	lead_data["created_at"] = current_timestamp()

	with open(CURRENT_LEADS_FILENAME, "w", encoding="utf-8") as file:
		json.dump(lead_data, file, indent=2)

def choose_the_best_job(cv_texts, emails):
	if not emails:
		print("No emails to choose from.")
		return ""

	short_emails = []
	for email in emails:
		short_emails.append({
			"subject": email["subject"],
			"date": email["date"],
			"snippet": email["snippet"],
			"body_text": email["body_text"][:3000],
		})

	template = load_prompt_template("data/joblead_prompt.txt")
	prompt = template.format(
		cv_texts=cv_texts[:3000],
		emails=short_emails
	)

	response = client.responses.create(
		model="gpt-4.1",
		input=prompt,
		max_output_tokens=1000,
	)

	print(response.output_text)
	write_jobleads_to_file(response.output_text)
	return response.output_text
