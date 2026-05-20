from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def get_embeddings(text_list):
    '''Return the text embeddings'''
    embeddings = model.encode(text_list, convert_to_tensor = True)
    return embeddings

def compute_similarity(cv_skills, job_skills):
    '''Comparing the similarity between the two embeddings'''
    cv_embeddings = get_embeddings(cv_skills)
    job_embeddings = get_embeddings(job_skills)
    similarities_matrix = util.cos_sim(cv_embeddings, job_embeddings)
    return similarities_matrix

'''util is for external data flow
core is for functionality processing external data
model is for external ai model'''