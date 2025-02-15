# app/utils/matching.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calcular_matching(candidato, vaga):
    candidato_texto = " ".join(candidato.habilidades + candidato.experiencias + candidato.formacoes)
    vaga_texto = " ".join(vaga.habilidades_desejadas + vaga.requisitos)

    vect = TfidfVectorizer()
    tfidf = vect.fit_transform([candidato_texto, vaga_texto])

    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return score
