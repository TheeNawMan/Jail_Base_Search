import argparse
import requests
import json

def get_jailbase_sources():
    url = "https://www.jailbase.com/api/1/sources/"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        sources = [source["source_id"] for source in json_data["records"]]
        return sources
    else:
        print("Error: HTTP status code ", response.status_code)
        return None

parser = argparse.ArgumentParser(description='Search for booking records on JailBase.')
parser.add_argument('last_name', type=str, help='The last name of the person to search for (e.g. smith)')

args = parser.parse_args()
sources = get_jailbase_sources()
for s in sources:
    url = f'https://www.jailbase.com/api/1/search/?source_id={s}&last_name={args.last_name}'
    response = requests.get(url)
    data = json.loads(response.text)

    for result in data['records']:
        print(result['book_date'], result['name'], result['charges'])