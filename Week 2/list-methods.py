# Manipulating lists using built-in methods

skills = ['Python', 'Java', 'C++', 'JavaScript']
print(f"Original list: {skills}")

# Adding a new skill to the list
skills.append("Odoo ERP")
print(f"After appending a new skill: {skills}")


# Inserting a skill at a specific index
skills.insert(0, "Computer Literacy")
print(f"After inserting a skill at index 0: {skills}")

# Removing a skill from the list
skills.remove("Java")
print(f"List with the removed item: {skills}")

skills.insert(-1, "Python")
skills.insert(-2, "Second Last")
print(f"Double occurrence list: {skills}")

skills.append("Word Press")

skills.remove("Python")
print("Removed double occurring item:", skills)

# Pop method
skills.pop(-1)
print(f"List of skills after pop method: {skills}")

skills.sort(reverse=True)
print(f"Sorted list: {skills}")