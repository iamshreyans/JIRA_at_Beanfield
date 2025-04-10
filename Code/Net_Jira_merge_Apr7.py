import pandas as pd

# Load the files
net = pd.read_excel('NET_PLAN_MILESTONE_MAR_2025_V2.0-7.xlsx', sheet_name='NET_PLAN_MILESTONE_MAR_V2.0')  # Adjust the path if needed
jira1 = pd.read_excel('/Users/c-shrsharma/Documents/JIRA/Jira_feb28(1).xlsx')  # Adjust the path if needed
jira2 = pd.read_excel('/Users/c-shrsharma/Documents/JIRA/Jira_April1.xlsx')  # Adjust the path if needed

# Concatenate both Jira files and drop duplicates based on 'JIRA_CONST_TICKET_ID'
jira_combined = pd.concat([jira1, jira2]).drop_duplicates(subset='JIRA_CONST_TICKET_ID', keep='first')

# Get all unique JIRA_CONST_TICKET_ID from net (after splitting any concatenated ticket IDs)
net_ticket_ids = net['JIRA_CONST_TICKET_ID'].str.split(',').explode().str.strip().unique()

# Get all unique JIRA_CONST_TICKET_ID from the combined Jira files
jira_ticket_ids = jira_combined['JIRA_CONST_TICKET_ID'].unique()

# Find missing tickets from net (those in Jira but not in net)
missing_tickets = set(jira_ticket_ids) - set(net_ticket_ids)

# Return the count of missing tickets
print(f"Number of missing tickets: {len(missing_tickets)}")

# jira_combined.to_excel('jira_combined.xlsx', index=False)  # Save the combined Jira data for reference

# # Create a dictionary to map ticket IDs to Jira data (aggregating for multiple entries)
# ticket_mapping = jira_combined.set_index('JIRA_CONST_TICKET_ID').to_dict(orient='index')

# # Split the 'JIRA_CONST_TICKET_ID' in 'net' but keep it as a string of concatenated IDs
# net_split = net.copy()
# net_split['JIRA_CONST_TICKET_ID'] = net_split['JIRA_CONST_TICKET_ID'].str.split(',')

# # Ensure that ticket_ids is always a list and handle any NaN or invalid types
# def map_ticket_data(ticket_ids):
#     # If ticket_ids is NaN or not a list, return an empty list
#     if isinstance(ticket_ids, str):  # Check if it's a string before splitting
#         ticket_ids = ticket_ids.split(',')
#     elif not isinstance(ticket_ids, list):  # If it's not a list, skip or return empty
#         return []
    
#     mapped_data = []
#     for ticket in ticket_ids:
#         ticket = ticket.strip()  # Clean up any spaces
#         if ticket in ticket_mapping:
#             mapped_data.append(ticket_mapping[ticket])
#         else:
#             mapped_data.append({col: None for col in ticket_mapping.get(ticket, {}).keys()})
#     return mapped_data

# # Apply the mapping to each row
# net_split['mapped_data'] = net_split['JIRA_CONST_TICKET_ID'].apply(map_ticket_data)

# # Flatten the 'mapped_data' and merge it back to the net file, preserving original rows
# net_split = net_split.explode('mapped_data', ignore_index=True)

# # Now, split the 'mapped_data' back into separate columns
# mapped_df = pd.json_normalize(net_split['mapped_data'])
# net_split = pd.concat([net_split.drop(columns='mapped_data'), mapped_df], axis=1)

# # Save the final merged file
# net_split.to_excel('merged_net_Jira.xlsx', index=False)

# print("Merge completed and saved as 'merged_net_Jira.xlsx'.")