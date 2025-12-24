def make_account(initial_balance):
    ### Replace with your own code (begin) ###
    balance = initial_balance

    def deposit(amount):
        nonlocal balance

        if type(amount) not in (int, float): #better? if not isinstance(amount, (int, float)):
            raise TypeError("Input must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        balance += amount
        return balance
    
    def withdraw(amount):
        nonlocal balance

        if type(amount) not in (int, float):
            raise TypeError("Input must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        if amount > balance:
            raise ValueError("Insufficient account balance.")
        
        balance -= amount
        return balance
    return deposit, withdraw
    pass
    ### Replace with your own code (end)   ###
