import re
import json
BOOKS_FILE="books.json"

def load_books():
    try:
        with open(BOOKS_FILE,"r") as f:
            data=json.load(f)
    except:
        data=[]
    return data

def save_books(data):
    with open(BOOKS_FILE,"w") as f:
        json.dump(data,f,indent=2)

def add_book():
    data=load_books()
    ids={b["id"] for b in data}
    bid=input("Book ID: ").strip()
    if bid in ids:
        print("Duplicate ID, not added.")
        return
    name=input("Name: ").strip()
    author=input("Author: ").strip()
    category=input("Category: ").strip()
    data.append({"id":bid,"name":name,"author":author,"category":category})
    save_books(data)
    print("Added")

def search_books():
    data=load_books()
    key=input("Enter regex keyword: ").strip()
    try:
        pat=re.compile(key,re.I)
    except Exception as e:
        print("Invalid regex")
        return
    found=[b for b in data if pat.search(b["name"]) or pat.search(b["author"]) or pat.search(b["category"])]
    if not found:
        print("No matches")
        return
    for b in found:
        print(b["id"],b["name"],b["author"],b["category"])

def update_book():
    data=load_books()
    bid=input("ID to update: ").strip()
    for b in data:
        if b["id"]==bid:
            b["name"]=input("New name: ").strip()
            b["author"]=input("New author: ").strip()
            b["category"]=input("New category: ").strip()
            save_books(data)
            print("Updated")
            return
    print("ID not found")

def delete_book():
    data=load_books()
    bid=input("ID to delete: ").strip()
    new=[b for b in data if b["id"]!=bid]
    if len(new)==len(data):
        print("ID not found")
        return
    save_books(new)
    print("Deleted")

def show_all():
    data=load_books()
    if not data:
        print("No books")
        return
    for b in data:
        print(b["id"],b["name"],b["author"],b["category"])

def main():
    while True:
        print("1 Add 2 Search 3 Update 4 Delete 5 Show 6 Exit")
        c=input("Choice: ").strip()
        if c=="1":
            add_book()
        elif c=="2":
            search_books()
        elif c=="3":
            update_book()
        elif c=="4":
            delete_book()
        elif c=="5":
            show_all()
        elif c=="6":
            break
        else:
            print("Invalid")

if __name__=="__main__":
    main()
