"""""""""
Suppose an individual is taxed 30% if earnings for a given week are > = $2,000. 
If earnings land < $2,000 for the week, the individual is taxed at a lower rate of 15%.

Write a function using Python to calculate both the pre-tax and post-tax earnings for a given individual, 
with the ability to feed in the hourly wage and the weekly hours as inputs.

For example, if an individual earns $55/hour and works for 40 hours, the function should return:
Pre-tax earnings were 55*40 = $2,200 for the week.
Post-tax earnings were $2,200*.7 (since we fall in higher tax bracket here) = $1,540 for the week
"""


def get_earnings(hourly_wage, weekly_hours):
    pre_tax = hourly_wage * weekly_hours
    post_tax = pre_tax * 0.7 if pre_tax > 2000 else pre_tax * 0.85
    return pre_tax, post_tax


print(get_earnings(hourly_wage=55, weekly_hours=40))
print(get_earnings(hourly_wage=55, weekly_hours=20))
print(get_earnings(hourly_wage=0, weekly_hours=20))
