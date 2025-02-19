import argparse
from googleapiclient.discovery import build
from rocchio import RocchioAlgo

def query_api(google_api_key, google_engine_id, query):
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build(
        "customsearch", "v1", developerKey=google_api_key
    )

    res = (
        service.cse()
        .list(
            q=query,
            cx=google_engine_id,
            num=10
        )
        .execute()
    )

    results = []
    if "items" in res:
        for item in res["items"]:
            results.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "description": item.get("snippet"),
                "content": f"{item.get('title', '')} {item.get('snippet', '')}"  # combined content for TF-IDF
            })
    return results


def main(google_api_key, google_engine_id, precision, query):
    rocchio = RocchioAlgo()
    # print(query)

    while True:

        # get search results
        query_results = query_api(google_api_key, google_engine_id, query)
        if not query_results:
                print("No results found.")
                break
        
        ## CALL SOME USER FEEDBACK FUNCTION ##

        ## CALCULATE PRECISION ##

        ## GET EXPANDED QUERY ##

        # for idx, result in enumerate(query_results, 1):
        #     print(f"{idx}. {result['title']}")
        #     print(f"   Link: {result['link']}")
        #     print(f"   Description: {result['description']}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="COMSW6111 - Project 1")
    
    parser.add_argument("google_api_key", type=str, help="First parameter (string)")
    parser.add_argument("google_engine_id", type=str, help="Second parameter (integer)")
    parser.add_argument("precision", type=float, help="Third parameter (float)")
    parser.add_argument("query", type=str, help="Fourth parameter (boolean)")

    args = parser.parse_args()

    main(args.google_api_key, args.google_engine_id, args.precision, args.query)