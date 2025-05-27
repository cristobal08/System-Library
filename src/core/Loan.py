class Loan:
    def __init__(self, id_loan, borrow_book, user_reference, loan_date, expect_return_date, state):
        self.id_loan = id_loan
        self.borrow_book = borrow_book
        self.user_reference = user_reference
        self.loan_date = loan_date
        self.expect_return_date = expect_return_date
        self.state = state
    
    def calculate_remain_days(self):
        print("Calculate remaining days")
    

    def check_expiration(self):
        print("Check if it is expired")
    
    def apply_renewal(self):
        print("Apply renewal")
    
    def register_return(self):
        print("Register return")