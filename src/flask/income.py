def calc_interest(amount, rate):
	if( rate != 0 ): return amount*rate
	else: return 0

def calc_income():
	gross_wages = 100000
	taxable_interest = 15000
	dividends = 5000
	qualified_dividends = 2500
	ira_deduction = 10000
	student_loan_interest = 4000
	
	income = ( gross_wages +
		taxable_interest +
		( dividends - qualified_dividends ) -
		ira_deduction -
		student_loan_interest )
	return income