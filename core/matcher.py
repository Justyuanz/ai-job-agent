from model.embeddings import compute_similarity

#enumerate
def match_skills(cv_skills, job_skills):
	'''Core AI matching logic'''
	similarity_matrix = compute_similarity(cv_skills, job_skills)
	matched = []
	maybe_matched = []
	missing = []
	for job_index, job_skill in enumerate(job_skills):
		scores_for_this_job_skill = similarity_matrix[:, job_index]
		max_score = max(scores_for_this_job_skill).item()
		if max_score > 0.9:	
			matched.append(job_skill)
		elif max_score > 0.5 and max_score <= 0.9:
			maybe_matched.append(job_skill)
		else:
			missing.append(job_skill)
	return matched, maybe_matched, missing

	