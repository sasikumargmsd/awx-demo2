import json

def custom_filter(data_list):
    transformed_data = []
    for item in data_list:
        transformed_item = {
            'name': item['name'].upper(),
            'age_category': 'Young' if item['age'] < 30 else 'Adult',
            'department': item['department']
        }
        transformed_data.append(transformed_item)
    return transformed_data

def export_filtered_data(filtered_data):
    with open("output.json", "w") as outfile:
        outfile.write(json.dumps(filtered_data))
    return "Exported users data into users.csv"

class FilterModule(object):
    def filters(self):
        return {
            'custom_filter': custom_filter,
            'export_filtered_data': export_filtered_data
        }
