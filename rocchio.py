# rocchio.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize
import numpy as np
import re

def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return set(word.strip().lower() for word in f.readlines())

class RocchioAlgo:
    def __init__(self, alpha=1.0, beta=0.75, gamma=0.15, stopwords_file="./proj1-stop.txt"):
        # weight for original query vector
        self.alpha = alpha

        # weight for relevant documents
        self.beta = beta

        # weight for non-relevant documents
        self.gamma = gamma

        self.stopwords = load_stopwords(stopwords_file)
        self.vectorizer = TfidfVectorizer()
        
    def expand_query(self, query, relevant_docs, irrelevant_docs):
        # create corpus with query first, followed by documents
        corpus = relevant_docs + irrelevant_docs
        
        # generate TF-IDF matrix
        tfidf_matrix = self.vectorizer.fit_transform(corpus)
        feature_names = np.array(self.vectorizer.get_feature_names_out())

        query_terms = set(query.lower().split())
        query_vector = np.zeros(len(feature_names))

        for idx, term in enumerate(feature_names):
            if term in query_terms:
                query_vector[idx] = 1 

        relevant_vectors = tfidf_matrix[0:len(relevant_docs)].toarray()
        irrelevant_vectors = tfidf_matrix[len(relevant_docs):].toarray()
        
        # calculate centroids
        relevant_centroid = np.zeros_like(query_vector)
        irrelevant_centroid = np.zeros_like(query_vector)
        
        if len(relevant_docs) > 0:
            relevant_centroid = np.mean(relevant_vectors, axis=0)
        if len(irrelevant_docs) > 0:
            irrelevant_centroid = np.mean(irrelevant_vectors, axis=0)
            
        # apply Rocchio
        modified_vector = (self.alpha * query_vector + 
                         self.beta * relevant_centroid - 
                         self.gamma * irrelevant_centroid)
        
        modified_vector = normalize(modified_vector.reshape(1, -1), norm='l2').flatten()
        
        # get term weights
        term_weights = list(zip(feature_names, modified_vector))
        term_weights.sort(key=lambda x: x[1], reverse=True)

        # filter existing query terms and non-alphabetic terms
        all_weighted_terms = []
        new_terms = []

        for term, weight in term_weights:
                    # Check if term is in the original query
                    if term.lower() in query_terms and weight > 0:
                        all_weighted_terms.append((term, weight, True))  # True = original query term
                    # For new terms, only consider alphabetic terms with positive weight
                    elif bool(re.search(r'[a-zA-Z]', term)) and weight > 0:
                        all_weighted_terms.append((term, weight, False))  # False = new term
                        new_terms.append((term, weight))
                        if len(new_terms) == 2:  # Still limit new terms to 2
                            break
        
        all_weighted_terms.sort(key=lambda x: x[1], reverse=True)
        
        return all_weighted_terms
        
        # candidate_terms = [term for term, _ in term_weights if term.lower() not in query_terms]
        # filtered_expansion_terms = [term for term, _ in expansion_terms if term not in self.stopwords]

        # if not filtered_expansion_terms:
        #     filtered_expansion_terms = next((term for term in candidate_terms if term.lower() not in self.stopwords), [])

        # return filtered_expansion_terms
    
    def get_expanded_query(self, query, relevant_docs, irrelevant_docs):
        weighted_terms = self.expand_query(query, relevant_docs, irrelevant_docs)
        if not weighted_terms:
            return query.split()
        
        # Extract just the terms from the weighted terms list
        ordered_terms = [term for term, _, _ in weighted_terms]
        
        # Add original query terms that might be missing
        original_terms = query.lower().split()
        for term in original_terms:
            if term not in [t.lower() for t in ordered_terms]:
                ordered_terms.append(term)
        
        return ordered_terms
