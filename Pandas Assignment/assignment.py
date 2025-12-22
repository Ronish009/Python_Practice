"""Assignment in Pandas"""
import pandas as pd

data = {
    'emp_id': [75, 33, 13, 45, 22],
    'emp_name': ['Ronish', 'Amit', 'Charlie', 'David', 'Eve'],
    'salary': [70000, 64000, 15000, 90000, 72000],
    'department': ['IT', 'HR', 'IT', 'Finance', 'IT'],
    'skills_set': [
        ['Python', 'SQL','Recruitment','GENAI'],
        ['Recruitment', 'Communication','Python','GENAI'],
        ['Java', 'Spring','SQL','GENAI'],
        ['Accounting', 'Excel','Java','Python','Recruitment'],
        ['Python', 'Data Analysis','Python','GENAI']
    ],
    'assignedornot': [True, False, True, True, False],
    'client_name': ['Client_R', None, 'Client_C', 'Client_R', None]
}

#View DataFrame
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame(data)
print("\n"+"#"*100+"\n")
print("DataFrame : \n\n",df)
print("\n"+"#"*100+"\n")

#To find for each department, the employee with the highest salary
print("To find for each department, the employee with the highest salary (Normal Way) :")
print("")
print(df.sort_values(by='salary', ascending=False).groupby("department").first())

print("\n"+"#"*100+"\n")

#employees who are in “GenAI” in and are already assigned to a client
print("\n\nemployees who are in “GenAI” in and are already assigned to a client :\n\n")
genai_assigned = df[
    df['skills_set'].apply(lambda skills: 'GENAI' in skills) &
    (df['assignedornot'])
]
print(genai_assigned)

print(genai_assigned)

print("\n\nemployees who are in “GenAI” in and are already assigned to a client in Other way:")

genai_assigned1 = df[df['skills_set'].apply(lambda s: 'GENAI' in s) & df['assignedornot']]
print(genai_assigned)



print("\n"+"#"*100+"\n")
# Create another column with summarized skill set
print("Create another column with summarized skill set : ")
df['skills_summary'] = df['skills_set'].apply(', '.join)

df['skills_count'] = df['skills_set'].apply(len)

# View the DataFrame

print("Updated DataFrame : \n\n",df)

print("\n"+"#"*100+"\n")

#who are the employees having python skill and what are the salaries
print("who are the employees having python skill and what are the salaries\n\n")
df_result=df[df['skills_set'].apply(lambda p: 'Python' in p)]
print(df_result[['emp_name','salary']])

print("\n"+"#"*100+"\n")

print("Manger Report")

#Total Number of Employee
count=df['emp_name'].count()
print("Total no of Employee : ", count)

#Number of employees assigned to a client
emp_client_count=df[df['assignedornot']]['emp_name'].count()
print("Number of employees assigned to a client : ",emp_client_count)

#Number of employees per client
count3=df[df['client_name'].notna()].groupby('client_name')['emp_id'].count()
print("Number of employees per client : \\n",count3)