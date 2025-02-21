# rocchio.py
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re

class RocchioAlgo:
    def __init__(self, alpha=1.0, beta=0.75, gamma=0.15):
        # weight for original query vector
        self.alpha = alpha

        # weight for relevant documents
        self.beta = beta

        # weight for non-relevant documents
        self.gamma = gamma
        self.vectorizer = TfidfVectorizer(stop_words='english')
        
    def expand_query(self, query, relevant_docs, irrelevant_docs):
        # create corpus with query first, followed by documents
        corpus = [query] + relevant_docs + irrelevant_docs
        
        # generate TF-IDF matrix
        tfidf_matrix = self.vectorizer.fit_transform(corpus)
        feature_names = np.array(self.vectorizer.get_feature_names_out())
        
        # extract vectors
        query_vector = tfidf_matrix[0].toarray().flatten()
        relevant_vectors = tfidf_matrix[1:len(relevant_docs)+1].toarray()
        irrelevant_vectors = tfidf_matrix[len(relevant_docs)+1:].toarray()
        
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
        
        # get term weights
        term_weights = list(zip(feature_names, modified_vector))
        term_weights.sort(key=lambda x: x[1], reverse=True)
        
        # filter existing query terms and non-alphabetic terms
        query_terms = set(query.lower().split())
        new_terms = []
        for term, weight in term_weights:
            if (term.lower() not in query_terms and 
                re.match(r'^[a-zA-Z]+$', term) and 
                weight > 0):
                new_terms.append((term, weight))
                if len(new_terms) == 2:  # Get top 2 new terms
                    break
                    
        return query_terms, new_terms
    
    def get_expanded_query(self, query, relevant_docs, irrelevant_docs):
        """
        Get the expanded query string
        
        Returns:
        str: Expanded query string with new terms added
        """
        query_terms, new_terms = self.expand_query(query, relevant_docs, irrelevant_docs)
        if not new_terms:
            return None
            
        # add new terms to query
        expanded_terms = list(query_terms) + [term for term, _ in new_terms]
        return ' '.join(expanded_terms)
