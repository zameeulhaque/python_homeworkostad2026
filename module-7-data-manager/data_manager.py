# 📌 Step 2: Program Introduction
print("Welcome to Smart Contact & Inventory Manager")

# 📌 Step 3: Contact Book (Dictionary)

contacts = {}

num_contacts = int(input("How many contacts do you want to add? : "))

for i in range(num_contacts):
    name = input("Enter Name: ").strip().lower()
    phone = input("Enter Phone Number: ")

    contacts[name] = phone

# 📌 Step 4: Display All Contacts

print("\nAll Contacts:")

for name, phone in contacts.items():
    print(name, "-", phone)

# 📌 Step 5: Update and Delete Contact

update_name = input("\nWhich contact do you want to update? : ").strip().lower()

if update_name in contacts:
    new_phone = input("Enter new phone number: ")
    contacts[update_name] = new_phone
else:
    print("Contact not found!")

delete_name = input("\nWhich contact do you want to delete? : ").strip().lower()

if delete_name in contacts:
    del contacts[delete_name]
else:
    print("Contact not found!")

print("\nUpdated Contact List:")

for name, phone in contacts.items():
    print(name, "-", phone)

# 📌 Step 6: Inventory Categories (Set)

categories = set()

num_categories = int(input("\nHow many categories do you want to add? : "))

for i in range(num_categories):
    category = input("Enter category: ")
    categories.add(category)

print("\nYour Categories:")
print(categories)

# 📌 Step 7: Set Operations

sample_categories = {"electronics", "food", "books"}

union_result = categories.union(sample_categories)
difference_result = categories.difference(sample_categories)

print("\nUnion:")
print(union_result)

print("\nDifference:")
print(difference_result)

# 📌 Step 8: Nested Dictionary (Advanced)

inventory = {
    "Laptop": {"price": 50000, "stock": 10},
    "Phone": {"price": 30000, "stock": 20},
    "Tablet": {"price": 40000, "stock": 30}
}

print("\nInventory Details:")

for product, details in inventory.items():
    print(
        f"{product} -> Price: {details['price']}, Stock: {details['stock']}"
    )

# 📌 Step 9: Debugging Practice

print("\nDebugging Practice")

# Missing Key
try:
    print(inventory["TV"])
except KeyError:
    print("KeyError: TV does not exist in inventory.")

# Duplicate Set Value
categories.add("electronics")
categories.add("electronics")

print("\nAfter adding duplicate value:")
print(categories)