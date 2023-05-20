#Customer_management_system
existing_customer = ['Juwon','Henry','Ayo']
New_customer_details = input("name: ")
for detail in existing_customer:
    if detail in New_customer_details:
        detail = True
    elif New_customer_details not in existing_customer:
        existing_customer.append(New_customer_details)
    else:
        print(existing_customer)



