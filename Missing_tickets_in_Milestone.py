import pandas as pd

# # Function to extract and split ticket values
# def extract_tickets(ticket_column):
#     # Split the concatenated tickets by comma (or any other separator, adjust as needed)
#     return set(ticket_column.str.split(',').explode().str.strip())

# # Load both files (Net and Jira files)
# net_file_path = 'NET_PLAN_MILESTONE_MAR_2025_V2.0-6.xlsx'  # Replace with your actual Net file path
# jira_file_path = '/Users/c-shrsharma/Documents/JIRA/Jira_Not_Merged_Feb28.xlsx'  # Replace with your actual Jira file path

# net_df = pd.read_excel(net_file_path, sheet_name='NET_PLAN_MILESTONE_MAR_V2.0')
# jira_df = pd.read_excel(jira_file_path)

# # Extract ticket values from the respective columns
# net_tickets = extract_tickets(net_df['JIRA_CONST_TICKET_ID'])
# jira_tickets = extract_tickets(jira_df['JIRA_CONST_TICKET_ID'])

# # Find missing tickets from Jira in Net
# missing_tickets_in_net = jira_tickets - net_tickets

# # Filter Jira data to get rows with missing tickets
# missing_ticket_data = jira_df[jira_df['JIRA_CONST_TICKET_ID'].apply(lambda x: any(ticket.strip() in missing_tickets_in_net for ticket in x.split(',')))]





# # Function to clean the address in the Summary column
# def clean_address(address):
#     # Regex pattern to detect parts before and after a hyphen, check for numeric or address range
#     if '-' in address:
#         parts = address.split('-')
#         # Handle the case where the first part before the hyphen is not numeric and remove it
#         if not parts[0].strip()[0].isdigit():
#             address = ' - '.join(parts[1:]).strip()  # Keep only the second part and onwards
        
#         # Handle the case where the second part after the hyphen is not numeric
#         elif len(parts) > 1 and not parts[1].strip()[0].isdigit():
#             address = parts[0].strip()  # Keep the first part if the second part is non-numeric

#     # Return the cleaned address
#     return address.strip()


# # Clean the "Summary" column
# missing_ticket_data['Cleaned_Summary'] = missing_ticket_data['Summary'].apply(clean_address)


# # Optionally, save the missing ticket data to a CSV file
# missing_ticket_data.to_excel('missing_ticket_data.xlsx', index=False)
# print("Missing ticket data saved to 'missing_ticket_data.csv'")
df=pd.read_excel('/Users/c-shrsharma/Documents/JIRA/missing_tickets_cleaned_address_for_GAPI.xlsx')






# Function to determine province
def get_province(ticket_id):
    if ticket_id.startswith('MTLCONST'):
        return 'Quebec'
    elif ticket_id.startswith('BCCONST'):
        return 'British Columbia'
    elif ticket_id.startswith('CONST'):
        return 'Ontario'
    else:
        return 'Unknown'

# Apply function to create new column
df['Province'] = df['JIRA_CONST_TICKET_ID'].apply(get_province)

df.to_excel('/Users/c-shrsharma/Documents/JIRA/missing_tickets_cleaned_address_for_GAPI_with_province.xlsx', index=False)