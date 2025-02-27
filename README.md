# InformationRetrieval
**Advanced Database Systems - Project 1**  

# README - Query Expansion using Google Custom Search API and Rocchio Algorithm

## Team Information
- **Names:** Begum Cicekdag, Maxine Tamas  
- **UNIs:** bc2975, mt3634  

## Submitted Files
- `query_expansion.py` - Main Python script implementing query expansion
- `rocchio.py` - Implementation of the Rocchio Algorithm
- `requirements.txt` - List of required Python libraries
- `README.md` - This documentation file
- `proj1-stop.txt` - List of all of our stop words

## How to Run the Program
This project is designed to run on a Google Cloud VM configured as per the provided setup instructions.

### Setup Instructions:
1. **Connect to Google Cloud VM:**
   ```sh
   ssh your-username@your-vm-ip
   ```
2. **Install Required Software:**
   ```sh
   sudo apt update
   sudo apt install python3-pip
   ```
3. **Clone the Repository:**
   ```sh
   git clone https://github.com/maxinetamas/InformationRetrieval.git
   cd InformationRetrieval
   ```
4. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
5. **Run the Program:**
   ```sh
   python3 query_expansion.py --query "your search query"
   ```

## Internal Design
The project consists of the following main components:
- **Query Expansion Module:** Implements the Rocchio Algorithm for query refinement.
- **Google Custom Search API Handler:** Handles search queries and fetches results.
- **Relevance Feedback Processor:** Analyzes results and selects relevant keywords.
- **Command-Line Interface:** Provides interaction for running queries and obtaining results.

### External Libraries Used
- `requests` - For making API calls to Google Custom Search
- `numpy` - For vector operations in the Rocchio Algorithm
- `json` - For handling API responses and configurations
- `argparse` - For parsing command-line arguments

### Query Modification Method

The core component of this project is the query expansion process using the Rocchio Algorithm, which follows these steps:

1. **Initial Query Execution:**

   The original query is sent to the Google Custom Search API.

2. **Relevance Feedback Collection:**

   The user marks each of the top-10 results as relevant (Y) or non-relevant (N).

3. **Vector-Based Query Adjustment:**

   The Rocchio Algorithm modifies the query vector by:
   - Increasing weights of terms from relevant results
   - Decreasing weights of terms from non-relevant results

4. **Term Reordering and Expansion:**

   Our enhanced implementation:
   - Reorders ALL terms (both original and new) based on their TF-IDF weights
   - Places the most discriminative terms first in the query
   - Adds up to 2 new high-weight terms not in the original query

5. **Iterative Refinement:**

   Steps 1-4 are repeated until the target precision is reached or no improvement is possible.

### Query Word Order Determination

Our implementation improves upon basic Rocchio by:
- Computing weights for all terms (original query + potential new terms)
- Sorting terms by their weight in descending order
- Creating a new query that maintains this weight-based ordering

This approach leverages the fact that search engines often give more weight to terms that appear earlier in the query.

### API Credentials

- **Google Custom Search API Key:** Required as the first command-line argument
- **Google Custom Search Engine ID:** Required as the second command-line argument

### Program Run Transcripts

Below is a sample transcript of the program's execution:

```bash
Parameters:
    Client key  = YOUR_GOOGLE_API_KEY
    Engine key  = YOUR_GOOGLE_ENGINE_ID
    Query       = machine learning
    Precision   = 0.8

Google Search Results:
======================
Result 1
[
 URL: https://example.com/1
 Title: Introduction to Machine Learning
 Summary: Machine learning is a subfield of artificial intelligence...
]
Relevant (Y/N)? Y
[results continued...]

FEEDBACK SUMMARY
Query: machine learning
Precision: 0.6
Still below the desired precision of 0.8
Indexing results...
Indexing results...
Augmenting by deep neural

Parameters:
    Client key  = YOUR_GOOGLE_API_KEY
    Engine key  = YOUR_GOOGLE_ENGINE_ID
    Query       = deep neural machine learning
    Precision   = 0.8

[second iteration continues...]