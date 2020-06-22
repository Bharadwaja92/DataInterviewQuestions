"""""""""
Suppose you're given the following table, called 'employees':


name	job_role
John	Analyst
Harry	Administrative Business Partner
Sam	Software Engineer
Tina	Analyst
To test your SQL skills, create a query that returns the 
name and job_role of each individual who has either a name that contains the letter 'a' or 
a job role that ends in the letters 'er'.
"""

sql_query = """
    SELECT name, job_role FROM table WHERE
    
    name LIKE '%a%' OR CHARINDEX('a', name) > 0 OR 
    
    job_role LIKE '%_er' OR RIGHT(job_role, 2) = 'er'     
"""

