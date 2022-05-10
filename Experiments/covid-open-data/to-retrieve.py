import pandas as pd
	
import requests
	
 
	
# Get the dataset metadata by passing package_id to the package_search endpoint
	
# For example, to retrieve the metadata for this dataset:
	
 
	
url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"
	
params = { "id": "64b54586-6180-4485-83eb-81e8fae3b8fe"}
	
package = requests.get(url, params = params).json()
	
print(package["result"])
	
 
	
# Get the data by passing the resource_id to the datastore_search endpoint
	
# See https://docs.ckan.org/en/latest/maintaining/datastore.html for detailed parameters options
	
# For example, to retrieve the data content for the first resource in the datastore:
	
print (package["result"]["resources"])
	
for idx, resource in enumerate(package["result"]["resources"]):
	
    if resource["datastore_active"]:
	
        url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/datastore_search"
	
        p = { "id": resource["id"] }
	
        data = requests.get(url, params = p).json()
	
        df = pd.DataFrame(data["result"]["records"])

        df.to_csv("downloaded_csv.csv")
	
        break
	
