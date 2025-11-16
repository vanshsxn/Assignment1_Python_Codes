def get_float(prompt):
    while True:
        try:
            v=input(prompt).strip()
            if v=="":
                return 0.0
            return float(v)
        except Exception as e:
            print("Invalid number, try again")

def categorize(percent):
    if percent <= 40:
        return "LOW", "Good control!"
    if percent <= 70:
        return "MODERATE", "Be careful!"
    return "HIGH", "Financial Risk!"

def main():
    try:
        income=get_float("Enter total monthly income: ")
        n=int(get_float("How many expense items? "))
        expenses=[]
        for i in range(n):
            desc=input(f"Expense {i+1} name: ").strip()
            amt=get_float(f"Expense {i+1} amount: ")
            expenses.append((desc, amt))
        total_exp=sum(a for _,a in expenses)
        savings=income-total_exp
        percent_spent=0.0 if income==0 else (total_exp/income)*100
        cat, msg=categorize(percent_spent)
        print("\nSUMMARY")
        print("Income:", income)
        print("Total Expenses:", total_exp)
        print("Savings:", savings)
        print(f"Percent Spent: {percent_spent:.2f}%")
        print("Spending Category:", cat)
        print("Advice:", msg)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__=="__main__":
    main()
