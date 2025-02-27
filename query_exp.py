import argparse
from googleapiclient.discovery import build
from rocchio import RocchioAlgo

def query_api(google_api_key, google_engine_id, query):
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build("customsearch", "v1", developerKey=google_api_key)

    try:
        search_res = (
            service.cse().list(
                q=query,
                cx=google_engine_id,
                num=10 # return only the top-10 results from the API
            ).execute()
        )
    except Exception as e:
        print(f"Error Fetching Search Results: {e}")


    html_results = []
    if "items" in search_res:
        for item in search_res["items"]:
            if "fileFormat" not in item:
                html_results.append({
                    "title": item.get("title"),
                    "link": item.get("link"),
                    "description": item.get("snippet"),
                    "content": f"{item.get('title', '')} {item.get('snippet', '')}"  # combined content for TF-IDF
                })
    return html_results

def get_user_feedback(query_results):
    rlvnt_docs = []
    irrlvnt_docs = []
    rlvnt_doc_cnt = 0
    for idx, result in enumerate(query_results, 1):
        print(f"""Result {idx}
        [
         URL: {result['link']}
         Title: {result['title']}
         Summary: {result['description']}
        ]""")
        relevance = input("Relevant (Y/N)?")
        if relevance == "Y" or relevance == "y":
            rlvnt_doc_cnt += 1
            rlvnt_docs.append(result['description'])
        else:
            irrlvnt_docs.append(result['description'])
    
    precision = rlvnt_doc_cnt / len(query_results)
    
    return precision, rlvnt_docs, irrlvnt_docs

def print_parameters(api_key, engine_id, precision, query):
    print(f"""Parameters:
    Client key  = {api_key}
    Engine key  = {engine_id}
    Query       = {query}
    Precision   = {precision}""")

def print_feedback_summary(query, cur_precision, desired_precision, expansion_terms):
    print(f"""
    FEEDBACK SUMMARY
    Query: {query}
    Precision: {cur_precision}
    Still below the desired precision of {desired_precision}
    Indexing results...
    Indexing results...
    Augmenting by {' '.join(expansion_terms)}
    """)

def main(google_api_key, google_engine_id, precision, query):
    rocchio = RocchioAlgo()
    original_query_terms = query.split()

    while True:
        print_parameters(google_api_key, google_engine_id, precision, query)

        query_results = query_api(google_api_key, google_engine_id, query)
        if not query_results:
            print("No HTML-pages have been returned within the top-10 results.")
            break
        
        print("Google Search Results:")
        print("======================")
        
        cur_precision, rlvnt_docs, irrlvnt_docs = get_user_feedback(query_results)

        if cur_precision == 0:
            print("The precision@10 of the results is zero.")
            break
    
        if cur_precision >= precision:
            print("Desired precision reached.")
            break

        updated_query, expansion_terms = rocchio.get_expanded_query(query, rlvnt_docs, irrlvnt_docs)
                
        print_feedback_summary(query, cur_precision, precision, expansion_terms)
                
        query = updated_query

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="COMSW6111 - Project 1")
    
    parser.add_argument("google_api_key", type=str)
    parser.add_argument("google_engine_id", type=str)
    parser.add_argument("precision", type=float)
    parser.add_argument("query", type=str)

    args = parser.parse_args()

    main(args.google_api_key, args.google_engine_id, args.precision, args.query)