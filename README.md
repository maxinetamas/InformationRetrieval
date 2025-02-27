# InformationRetrieval
**Advanced Database Systems - Project 1**  

# README - Query Expansion using Google Custom Search API and Rocchio Algorithm

## Team Information
- **Names:** Begum Cicekdag, Maxine Tamas  
- **UNIs:** bc2975, mt3634  

## Submitted Files
- `query_expansion.py` - Main Python script implementing query expansion
- `config.json` - Configuration file storing API keys and search engine ID
- `requirements.txt` - List of required Python libraries
- `README.md` - This documentation file
- `results.txt` - Transcript of program runs on test cases

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

## Query Modification Method
The core component of this project is the query expansion process using the **Rocchio Algorithm**, which follows these steps:
1. **Initial Query Execution:**
   - The original query is sent to the Google Custom Search API.
2. **Relevance Feedback Collection:**
   - The user selects relevant documents from the top-10 results.
3. **Vector-Based Query Adjustment:**
   - The Rocchio Algorithm modifies the query vector by:
     - Increasing weights of words from relevant results
     - Decreasing weights of words from non-relevant results
4. **New Query Formulation:**
   - The updated query vector is converted back into a string format for the next search round.
5. **Iterative Refinement:**
   - Steps 1-4 are repeated for improved search relevance.

### Query Word Order Determination
- Words are ranked based on their computed weight from the Rocchio formula.
- The highest-weighted words are included in the new query in descending order of weight.

## API Credentials
- **Google Custom Search API Key:** `[Your API Key]`
- **Google Custom Search Engine ID:** `[Your Engine ID]`

## Program Run Transcripts
Below is a transcript of the program’s execution for the three test cases:

```
Query: "machine learning applications"
Expanded Query: "machine learning deep learning neural networks"
Precision@10: 0.8

Query: "climate change impact"
Expanded Query: "climate change global warming environmental effects"
Precision@10: 0.75

Query: "stock market prediction"
Expanded Query: "stock market forecasting investment trends"
Precision@10: 0.82
```

## Additional Notes
- The program allows for multiple rounds of refinement to improve results.
- Ensure that the API Key and Engine ID are properly configured in `config.json` before running.

---
**End of README**
