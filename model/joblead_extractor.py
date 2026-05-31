from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def load_prompt_template(filename: str) -> str:
	try:
		file = open(filename, "r")
	except Exception as error:
		print("Failed to open prompt file:", error)
		return ""
	return file.read()

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
	return response.output_text
