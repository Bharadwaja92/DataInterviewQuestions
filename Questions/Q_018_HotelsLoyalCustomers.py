"""""""""
You are an analyst for a major US hotel chain which has locations all over the US. 
Your marketing team is planning a promotion focused around loyal customers, and they are trying to 
forecast how much revenue the promotion will bring in. 
However, they need help from you to understand how much revenue comes from "loyal" customer to plug into 
their model.

A "loyal" customer is defined as 
(1) having a memebership with your company's point system, 
(2) having >2 stays at each hotel the customer visited, 
(3) having stayed at 3 different locations throughout the US.

You have a table showing all transactions made in 2017. The schema of the table is below:

Table: customer_transactions
Column Name	        Data Type	Description
customer_id	        id	        id of the customer
hotel_id	        integer	    unique id for hotel
transaction_id	    integer	    id of the given transaction
first_night	        string	    first night of the stay, column format is "YYYY-mm-dd"
number_of_nights	integer	    # of nights teh customer stayed in hotel
total_spend	        integer	    total spend for transaction, in USD
is_member	        boolean	    indicates if the customer is a member of our points system

Can you write a query that calculates percent of revenue loyal customers brought in 2017? 
"""

cols = ['customer_id', 'hotel_id', 'transaction_id', 'first_night', 'number_of_nights', 'total_spend',
        'is_member']

# Get number of stays
count_query = 'SELECT customer_id, COUNT(transaction_id) FROM CUST_TABLE GROUP BY customer_id'
# Get locations of stays
location_query = 'SELECT customer_id, GROUP_CONCAT(hotel_id) FROM CUST_TABLE GROUP BY customer_id'

combined_query = 'SELECT customer_id, c1.count_txn, c2.hotel_list FROM CUST_TABLE WHERE ' \
                 'c1 in (SELECT COUNT(transaction_id) AS count_txn FROM CUST_TABLE GROUP BY customer_id) AND ' \
                 'c2 in (SELECT GROUP_CONCAT(hotel_id) FROM CUST_TABLE GROUP BY customer_id)'


