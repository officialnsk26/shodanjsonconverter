import jsonlines
import pandas as pd

# Function to filter the specified fields from the JSON data
def filter_fields(data):
    return {
        "ip_str": data.get("ip_str"),
        "hostnames": data.get("hostnames") if data.get("hostnames") != [''] else None,
        "country_name": data["location"].get("country_name") if "location" in data else None,
        "data": data.get("data"),
        "org": data.get("org"),
        "timestamp": data.get("timestamp"),
        "domains": data.get("domains") if data.get("domains") != [''] else None,
        "port": data.get("port"),
        "references": data.get("references"),
        "vulns": data.get("vulns")
    }

# Read JSON file with multiple entries using jsonlines
json_file_path = 'input.json'
filtered_data = []

with jsonlines.open(json_file_path) as reader:
    for entry in reader:
        filtered_data.append(filter_fields(entry))

# Create a DataFrame from the filtered data
df = pd.DataFrame(filtered_data)

# Save the DataFrame to an Excel file
df.to_excel('filtered_data.xlsx', index=False)

print("Filtered data has been saved to filtered_data.xlsx")
