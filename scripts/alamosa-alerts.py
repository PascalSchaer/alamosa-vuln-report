import os
import csv
import shodan

API_KEY = os.getenv("SHODAN_API_KEY")  # env variable for API key
api = shodan.Shodan(API_KEY)

ORG_LIST = [
    "Adams State University",
    "San Luis Valley Health",
    "SLV Health",
    "SLV Regional Medical Center",
    "Trinidad State College",
    "Alamosa School District",
    "Centauri Schools",
    "City of Alamosa",
    "Alamosa County",
    "Jade Communications",
    "Conejos County Hospital",
    "Rio Grande Hospital"
]

def search_targets():
    for org in ORG_LIST:
        print(f"\nSearching for: {org}")
        query = f'city:"Alamosa" country:"US" org:"{org}"'
        try:
            results = api.search(query)
            print(f"Found {results['total']} results")
            for result in results['matches']:
                ip = result['ip_str']
                org = result.get('org', 'N/A')
                port = result['port']
                product = result.get('product', 'Unknown')
                print(f"[{ip}] - {product} on port {port} (Org: {org})")
        except shodan.APIError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    search_targets()