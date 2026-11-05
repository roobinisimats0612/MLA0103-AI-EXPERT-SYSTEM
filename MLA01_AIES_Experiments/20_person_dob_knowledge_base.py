"""Fictional sample records only."""
PEOPLE = {"Asha": "2005-04-12", "Ravi": "2004-11-03", "Mina": "2005-08-25"}

if __name__ == "__main__":
    print("Demo uses fictional records.")
    choice = input("Search by (1) name or (2) DOB? ")
    if choice == "1":
        name = input("Name: ").strip().title()
        print("DOB:", PEOPLE.get(name, "No record found"))
    elif choice == "2":
        dob = input("DOB (YYYY-MM-DD): ").strip()
        print("Names:", [name for name, date in PEOPLE.items() if date == dob])
    else:
        print("Invalid choice.")
