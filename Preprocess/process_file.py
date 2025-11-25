import pandas as pd
import json
from convert import convert_to_jsonl


data = pd.read_excel('C:\\Users\\G705762\\OneDrive - General Mills\\Desktop\\ServiceNowTicketAutomation\\Data\\past_incidents.xlsx')

incidents = pd.DataFrame(data)

with open('..\\Data\\incidents.jsonl', 'w') as file:
    for incident in incidents.iterrows():
        incident_jsonl = convert_to_jsonl(incident[1])
        file.write(json.dumps(incident_jsonl) + '\n')