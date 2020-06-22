"""""""""
Suppose you are given a SQL table containing the brands of shoes (field name: brand) as well as 
the shoe price (field name: price). The database is called shoe_info. 
You are tasked with updating the prices in this database for a few brands of shoes. 
Specifically, you have been asked to update 
all Nike shoe prices to $100, and all Adidas shoe prices to $85. Using SQL, write a query to perform this action.
"""

sql_query1 = """
    UPDATE shoe_info 
    SET shoe_info.price = 100 WHERE shoe_info.brand = "Nike"
    
    UPDATE shoe_info 
    SET shoe_info.price = 85 WHERE shoe_info.brand = "Adidas"    
"""

sql_query2 = """
    UPDATE shoe_info 
    SET shoe_info.[price] = 
        (CASE 
            WHEN shoe_info.brand = "Nike" THEN 100
            WHEN shoe_info.brand = "Adidas" THEN 85 
        END)
    WHERE shoe_info.brand in ("Nike", "Adidas")
"""
