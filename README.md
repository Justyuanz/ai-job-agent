# AI Job Agent

This is a small MVP for helping me choose and prepare for job applications.

The goal is simple:

1. Check my Gmail for recent LinkedIn job alert emails.
2. OpenAI to chooses two promising job leads for me bases on the emails.
3. Save those two leads so I can inspect them.
4. I put the full job description into `data/job_ad.txt`.
5. SentenceTransformer compares the job ad with my CV.
6. OpenAI gives practical feedback for my CV and application angle.

## Models Used

- `gpt-4.1` chooses the job leads from Gmail emails.
- `sentence-transformers/all-MiniLM-L6-v2` from Hugging Face compares CV skills and job skills with embeddings.
- `gpt-5.5` is currently used for the CV and job feedback.

## Current Limitations

This MVP does not scrape full job descriptions yet.

The next goal is to scrape full job description and make this run every two days and manage old leads more cleanly.
