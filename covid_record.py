import os
import csv

FNAME="vaccination_records.csv"
HEADERS=["Name","Age","Gender","Vaccine","Dose","Date","ID"]

def ensure_file():
    if not os.path.exists(FNAME):
        with open(FNAME,"w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(HEADERS)

def add_record():
    try:
        ensure_file()
        name=input("Name: ").strip()
        age=input("Age: ").strip()
        gender=input("Gender: ").strip()
        vaccine=input("Vaccine: ").strip()
        dose=input("Dose (1/2/Booster): ").strip()
        date=input("Date (YYYY-MM-DD): ").strip()
        idno=input("Record ID: ").strip()
        with open(FNAME,"a",newline="") as f:
            writer=csv.writer(f)
            writer.writerow([name,age,gender,vaccine,dose,date,idno])
        print("Record appended.")
    except Exception as e:
        print("Error:",e)

def read_all():
    try:
        ensure_file()
        with open(FNAME,"r",newline="") as f:
            reader=list(csv.reader(f))
        if not reader or len(reader)<=1:
            print("No records found.")
            return
        cols=list(zip(*reader))
        widths=[max(len(str(x)) for x in col) for col in cols]
        for row in reader:
            print("  ".join(str(x).ljust(w) for x,w in zip(row,widths)))
    except Exception as e:
        print("Error:",e)

def main():
    while True:
        print("1 Add  2 Show  3 Exit")
        c=input("Choice: ").strip()
        if c=="1":
            add_record()
        elif c=="2":
            read_all()
        elif c=="3":
            break
        else:
            print("Invalid")

if __name__=="__main__":
    main()
