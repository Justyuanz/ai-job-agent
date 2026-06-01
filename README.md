# AI Job Agent

AI Job Agent is a personal AI-assisted workflow that helps me choose and prepare for job applications without feeling overwhelmed.

The project reads recent LinkedIn job-alert emails from Gmail, uses OpenAI to select promising job leads, compares a job description with my CV using sentence embeddings, and generates practical feedback for my application.

This is currently an MVP. The goal is not to auto-apply to hundreds of jobs, but to help me focus on a small number of relevant opportunities and apply with better preparation.

---

## Why I Built This

Job hunting can become overwhelming, especially when there are too many job alerts and limited time.

I wanted to build a small AI workflow that helps me answer:

- Which job from my recent alerts is actually worth looking at?
- How well does this job match my current CV?
- Which skills or experiences from my CV are relevant?
- What is missing?
- How should I improve my CV or application angle for this job?

The long-term goal is to make job hunting feel more consistent and less stressful by helping me focus on one relevant job at a time.

---

## Current Workflow

The current MVP works like this:

1. The Python script checks my Gmail for recent LinkedIn job-alert emails.
2. OpenAI reads the email content and selects two promising job leads.
3. The selected leads are saved so I can inspect them manually.
4. I copy the full job description into `data/job_ad.txt`.
5. `sentence-transformers/all-MiniLM-L6-v2` compares the job description with my CV using an embedding model.
6. OpenAI generates practical feedback for my CV and application angle.

---

## Example Output

Example feedback:

```text
Verdict: Worth applying.

Strong matches:
- Python
- API integration
- Git/GitHub
- AI workflow experience
- Project-based learning background

Missing or weaker areas:
- Docker
- Cloud deployment
- Professional backend experience

1. Best application angle
2. Biggest gaps
3. CV changes
4. Cover letter angle

```

---

## Models Used

This project currently uses:

- `gpt-4.1` to select promising job leads from Gmail emails.
- `sentence-transformers/all-MiniLM-L6-v2` to compare the job description with my CV.
- `gpt-5.5` to generate CV feedback and application advice.

---

## Tech Stack

- Python
- Gmail API
- OpenAI API
- SentenceTransformers
- Hugging Face models
- dotenv
- Markdown/text file output

---

## Current Features

- Reads recent job-alert emails from Gmail.
- Uses OpenAI to select promising job leads.
- Saves selected leads for manual review.
- Compares a full job description with my CV using sentence embeddings.
- Generates application feedback with OpenAI.
- Helps identify matching skills, missing skills, and CV improvement ideas.

---

## Current Limitations

This project is still an MVP.

Current limitations:

- Full job descriptions are added manually through `data/job_ad.txt`.
- The workflow is not fully scheduled yet.
- It does not currently send Telegram notifications.
- It does not yet store job history in a database.

---

## Future Improvements

Planned improvements:

- Add automatic scheduling to run every two days.
- Add Telegram notifications with the best job and application summary.
- Add SQLite database storage for job history and deduplication.
- Generate Markdown reports for each analyzed job.
- Add a custom scoring system for job relevance.
- Add automatic full job-description fetching where possible.
- Add application status tracking.
- Add cover letter draft generation.
- Add a small dashboard for job history and match scores.

---

## What I Learned

Through this project, I practiced:

- Python
- Working with external APIs
- Reading and processing Gmail data
- Using OpenAI for structured decision-making
- Using embeddings for text similarity
- Designing an AI-assisted workflow
- Building a practical automation tool for a real personal problem

---

## Status

Current status: MVP in progress.

The core idea works, but the project is still being improved step by step.
