
from transformers import pipeline
from openai import OpenAI

'''use text generation in hugging face, can search google FLAN'''
def generate_feedback(cv_text, job_text, missing_skills):
	'''compare the CV test with job text and suggests improvement reviewing the missing skills'''

	prompt = f"""
Analyze the CV against the job description and provide detailed feedback.
JOB DESCRIPTION:
{job_text}

CV:
{cv_text}

MISSING SKILLS:
{missing_skills}

Give your response in this structured format:

1. Overall Match Evaluation(short paragraph)

2. Key Weaknesses:
- bullet points

3. Missing Skills Impact
- explain how missing skills affect the candidate

4. Specific Improvements
- what exactly to add/change in CV

5. ATS Optimization Tips
- formatting + keyword advice

Be specific, avoid generic advice.
"""
	messages = [
    {"role": "system", "content": "You are a professional CV reviewer and ATS optimization expert."},
    {"role": "user", "content": prompt},
	]
	#chatbot = pipeline("text-generation", model="MiniMaxAI/MiniMax-M2.7")
	#chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")
	#response = chatbot(messages)

	client = OpenAI()

	response = client.responses.create(
		model="gpt-5.5",
		input=[
			{
				"role": "user",
				"content": [
					{
						"type": "input_text",
						"text": "What teams are playing in this image?",
					},
					{
						"type": "input_image",
						"image_url": "https://api.nga.gov/iiif/a2e6da57-3cd1-4235-b20e-95dcaefed6c8/full/!800,800/0/default.jpg"
					}
				]
			}
		]
	)

	print(response.output_text)
	return response
