import pandas as pd

data = [
    {"Name": "Tech Mahindra", "Email": "contact@techmahindra.com", "Website": "https://www.techmahindra.com", "LinkedIn": "https://www.linkedin.com/company/tech-mahindra", "Location": "Hyderabad"},
    {"Name": "Cyient", "Email": "info@cyient.com", "Website": "https://www.cyient.com", "LinkedIn": "https://www.linkedin.com/company/cyient", "Location": "Hyderabad"},
    {"Name": "ValueLabs", "Email": "info@valuelabs.com", "Website": "https://www.valuelabs.com", "LinkedIn": "https://www.linkedin.com/company/valuelabs", "Location": "Hyderabad"},
    {"Name": "Innominds", "Email": "info@innominds.com", "Website": "https://www.innominds.com", "LinkedIn": "https://www.linkedin.com/company/innominds", "Location": "Hyderabad"},
    {"Name": "Cigniti", "Email": "info@cigniti.com", "Website": "https://www.cigniti.com", "LinkedIn": "https://www.linkedin.com/company/cigniti-technologies", "Location": "Hyderabad"},
    {"Name": "Infosys", "Email": "info@infosys.com", "Website": "https://www.infosys.com", "LinkedIn": "https://www.linkedin.com/company/infosys", "Location": "Hyderabad"},
    {"Name": "TCS", "Email": "info@tcs.com", "Website": "https://www.tcs.com", "LinkedIn": "https://www.linkedin.com/company/tata-consultancy-services", "Location": "Hyderabad"},
    {"Name": "Wipro", "Email": "info@wipro.com", "Website": "https://www.wipro.com", "LinkedIn": "https://www.linkedin.com/company/wipro", "Location": "Hyderabad"},
    {"Name": "HCL", "Email": "info@hcl.com", "Website": "https://www.hcltech.com", "LinkedIn": "https://www.linkedin.com/company/hcl-technologies", "Location": "Hyderabad"},
    {"Name": "Cognizant", "Email": "info@cognizant.com", "Website": "https://www.cognizant.com", "LinkedIn": "https://www.linkedin.com/company/cognizant", "Location": "Hyderabad"},
    {"Name": "Accenture", "Email": "info@accenture.com", "Website": "https://www.accenture.com", "LinkedIn": "https://www.linkedin.com/company/accenture", "Location": "Hyderabad"},
    {"Name": "Capgemini", "Email": "info@capgemini.com", "Website": "https://www.capgemini.com", "LinkedIn": "https://www.linkedin.com/company/capgemini", "Location": "Hyderabad"},
    {"Name": "Deloitte", "Email": "info@deloitte.com", "Website": "https://www.deloitte.com", "LinkedIn": "https://www.linkedin.com/company/deloitte", "Location": "Hyderabad"},
    {"Name": "Mindtree", "Email": "info@mindtree.com", "Website": "https://www.mindtree.com", "LinkedIn": "https://www.linkedin.com/company/mindtree", "Location": "Hyderabad"},
    {"Name": "LTIMindtree", "Email": "info@ltimindtree.com", "Website": "https://www.ltimindtree.com", "LinkedIn": "https://www.linkedin.com/company/ltimindtree", "Location": "Hyderabad"},
    {"Name": "IBM", "Email": "info@ibm.com", "Website": "https://www.ibm.com", "LinkedIn": "https://www.linkedin.com/company/ibm", "Location": "Hyderabad"},
    {"Name": "Oracle", "Email": "info@oracle.com", "Website": "https://www.oracle.com", "LinkedIn": "https://www.linkedin.com/company/oracle", "Location": "Hyderabad"},
    {"Name": "Microsoft", "Email": "info@microsoft.com", "Website": "https://www.microsoft.com", "LinkedIn": "https://www.linkedin.com/company/microsoft", "Location": "Hyderabad"},
    {"Name": "Google", "Email": "info@google.com", "Website": "https://www.google.com", "LinkedIn": "https://www.linkedin.com/company/google", "Location": "Hyderabad"},
    {"Name": "Genpact", "Email": "info@genpact.com", "Website": "https://www.genpact.com", "LinkedIn": "https://www.linkedin.com/company/genpact", "Location": "Hyderabad"},
    {"Name": "Amazon", "Email": "info@amazon.com", "Website": "https://www.amazon.com", "LinkedIn": "https://www.linkedin.com/company/amazon", "Location": "Hyderabad"},
    {"Name": "Meta", "Email": "info@meta.com", "Website": "https://www.meta.com", "LinkedIn": "https://www.linkedin.com/company/meta", "Location": "Hyderabad"},
    {"Name": "Salesforce", "Email": "info@salesforce.com", "Website": "https://www.salesforce.com", "LinkedIn": "https://www.linkedin.com/company/salesforce", "Location": "Hyderabad"},
    {"Name": "Zoho", "Email": "info@zoho.com", "Website": "https://www.zoho.com", "LinkedIn": "https://www.linkedin.com/company/zoho-corporation", "Location": "Hyderabad"},
    {"Name": "ServiceNow", "Email": "info@servicenow.com", "Website": "https://www.servicenow.com", "LinkedIn": "https://www.linkedin.com/company/servicenow", "Location": "Hyderabad"}
]

df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)
df.fillna("Not Available", inplace=True)

df.to_excel("hyderabad_it_companies.xlsx", index=False)

print("Excel file with 25 entries created successfully!")
