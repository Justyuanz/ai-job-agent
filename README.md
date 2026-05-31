# AI Job Agent

Beginner-friendly MVP for an AI-assisted job application workflow.

The project does not try to apply to many jobs at once. Instead, it follows a smaller agent loop:

1. Read recent LinkedIn job-alert emails from Gmail.
2. Ask OpenAI to choose two promising job leads: a primary lead and a backup lead.
3. Save those leads to `data/current_leads.json`.
4. Wait for the user to open one lead and paste the full job description into `data/job_ad.txt`.
5. When `job_ad_ready` is set to `true`, compare the full job ad with the CV.
6. Ask OpenAI to write practical CV and application feedback.
7. Append the feedback to `data/feedback_report.md`.

## Current Workflow

Run the project:

```bash
python main.py
```

If there is no current lead file, the program searches Gmail for recent LinkedIn job-alert emails and creates:

```text
data/current_leads.json
```

That file includes the selected leads, a status, a `job_ad_ready` flag, and a `created_at` timestamp.

Then open the primary or backup LinkedIn lead manually. If the job looks suitable, paste the full job description into:

```text
data/job_ad.txt
```

Then change this field in `data/current_leads.json`:

```json
"job_ad_ready": true
```

Run the project again:

```bash
python main.py
```

The program extracts skills from the CV and job ad, compares them, sends the evidence to OpenAI, and appends a dated feedback report to:

```text
data/feedback_report.md
```

## Models Used

- `gpt-4.1` is used in `model/joblead_extractor.py` to choose the best job leads from Gmail job-alert emails.
- `gpt-5.5` is currently set in `model/reviewer.py` to generate CV and job feedback from the selected full job ad and skill matching data.

## Project Status

This is an MVP. The current version uses Gmail for lead discovery and manual pasting for the full job ad.

Planned next improvements:

- Add real two-day automation.
- Improve job lead state handling between runs.
- Add safer reset/archive behavior after a job has been reviewed.
- Add scraping or another reliable way to fetch full job descriptions automatically.
- Improve tests around skill extraction, matching, and JSON state files.

## Local Secrets

Secrets should stay local and should not be committed.

Expected local files:

```text
.env
.secrets/credentials.json
.secrets/token.json
```

The `.env` file should contain:

```text
OPENAI_API_KEY=your_key_here
```

