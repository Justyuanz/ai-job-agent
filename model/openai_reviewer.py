from openai import OpenAI

client = OpenAI()

def write_feedback_to_file(filename: str, text: str) -> None:
    if not text:
        print("No feedback to write.")
        return

    with open(filename, "a", encoding="utf-8") as file:
        file.write("\n\n--- NEW FEEDBACK REPORT ---\n\n")
        file.write(text)
        file.write("\n")

def load_prompt_template(filename: str) -> str:
	try:
		file = open(filename, "r")
	except Exception as error:
		print("Failed to open prompt file:", error)
	return file.read()

def generate_feedback(cv_texts: list[str],
					  job_texts: str,
					  cv_skills: list[str],
					  job_skills: list[str],
					  matched: list[str],
					  maybe_matched: list[str],
					  missing: list[str]) ->None:
	
	template = load_prompt_template("data/prompt.txt")
	prompt = template.format(
        cv_texts=cv_texts[:3000],
        job_texts=job_texts[:3000],
        cv_skills=cv_skills,
        job_skills=job_skills,
        matched=matched,
        maybe_matched=maybe_matched,
        missing=missing,
    )

	response = client.responses.create(
		model="gpt-5.5",
		input=prompt,
		max_output_tokens=500,
	)

	write_feedback_to_file("data/feedback_report.md", response.output_text)