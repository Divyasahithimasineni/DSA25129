def search_employee(emp_list, target, index=0):
    if index == len(emp_list):
        return -1

    if emp_list[index] == target:
        return index

    return search_employee(emp_list, target, index + 1)


employees = [101, 102, 103, 104, 105]

target = int(input("Enter employee ID to search: "))

result = search_employee(employees, target)

if result != -1:
    print("Employee ID found at position", result + 1)
else:
    print("Employee ID not found")
