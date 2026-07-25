# A contact book 

contacts = [
    {"name" : "Peter Mwangi", "phone" : "0794098715", "skills" : "Software Developer, Data Analyst", "location" : "Nairobi"},
    {"name" : "Isaac Jn", "phone" : "0796715672", "skills" : "Pilot", "location" : "South Africa"},
    {"name" : "Gish Helencia", "phone" : "0708919212", "skills" : "Skin Care Expert", "location" : "Los Angelas"},
    {"name" : "Peter Kibocha", "phone" : "0119298133", "skills" : "Business Merchant", "location" : "Asia"},
    {"name" : "Lydia Kuobi", "phone" : "+1 392 932 343", "skills" : "Diplomat", "location" : "Geneva"}
]

print("Contacts stored: ", len(contacts))

# for contact in contacts:
#     contact['name'] = "Steve Maina"
#     contact['phone'] = "0789238193"
#     contact['skills'] = "Electrical Engineer"
#     contact['location'] = "Kiambu"

# print("Updated contacts", contacts)

print()

print("======Contact Book======")

# enumerate() gives you both the index and the item as you loop. i is the index number
for i, contact in enumerate(contacts):
    print(f"\n {i+1}. {contact['name']}")
    print(f"    Phone - {contact['phone']}")
    print(f"    Skills - {contact['skills']}")
    print(f"    Location - {contact['location']}")

print()

# Add contact
contacts.append({"name" : "Steve Maina", "phone" : "0790291092", "skills" : "Electrical Engineer", "location" : "Nairobi"})

print("Updated contact list: ", len(contacts)," contacts")

print()

# Search by contact by name
search_name = input("Search contact? ")
found = False

for contact in contacts:
    if contact['name'] == search_name:
        print('Contact Found!')
        print(f"    Name: {contact['name']}")
        print(f"    Phone: {contact['phone']}")
        print(f"    Skills: {contact['skills']}")
        print(f"    Location: {contact['location']}")
        found = True

        delete_confirmation = input("Do you want to delete this contact? ")
        if delete_confirmation == "yes":
            contacts.pop(contact['name'] == search_name)

        break

if not found:
    print(f"Searched Contact {search_name} does not exist!")

print()


print("======Contact Book======")

# enumerate() gives you both the index and the item as you loop. i is the index number
for i, contact in enumerate(contacts):
    print(f"\n {i+1}. {contact['name']}")
    print(f"    Phone - {contact['phone']}")
    print(f"    Skills - {contact['skills']}")
    print(f"    Location - {contact['location']}")

print()

# # Deleting a contact
# contacts.remove({"name" : "Peter Mwangi", "phone" : "0794098715", "skills" : "Software Developer, Data Analyst", "location" : "Nairobi"})

# print(f"Contact Successfully deleted!")