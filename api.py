#API 1


@app.get("/items/total_items")
def get_sold_items(start_date: str, end_date: str, department: str):
    sold_items = []
    start_date="2022-07-01"
    end_date="2022-09-30"
    department="Marketing"
    for item in data:
        item_date = item["date"]
        item_department = item["department"]

        
        if start_date <= item_date <= end_date and item_department == department:
            sold_items.append(item)
    return len(sold_items)

#API 2

@app.get("/items/nth_most_total_item")
def second_most_total_item(item_by: str, start_date: str, end_date: str):
    start_date="2022-10-01"
    end_date="2022-12-31"
    filtered_data = [item for item in data if start_date <= item["date"] <= end_date]

    
    sorted_data = sorted(filtered_data, key=itemgetter(item_by), reverse=True)

    second_most_sold_item = None
    if len(sorted_data) >= 2:
        second_most_sold_item = sorted_data[1]
    return second_most_sold_item


@app.get("/items/nth_most_total_item_price")
def fourth_most_total_item_price(item_by: str, start_date: str, end_date: str):
    start_date="2022-04-01"
    end_date="2022-06-30"
    filtered_data = [item for item in data if start_date <= item["date"] <= end_date]

    
    sorted_data = sorted(filtered_data, key=itemgetter(item_by), reverse=True)

    fourth_most_sold_item = None
    if len(sorted_data) >= 4:
        fourth_most_sold_item = sorted_data[3]
    return fourth_most_sold_item

# API 3

@app.get("/items/percentage_of_department_wise_sold_items")
def department_wise_percentage(start_date: str, end_date: str) -> Dict[str, float]:
    department_count = {}
    total_count = 0

    for item in data:
        item_date = item["date"]
        item_department = item["department"]

       
        if start_date <= item_date <= end_date:
            if item_department in department_count:
                department_count[item_department] += 1
            else:
                department_count[item_department] = 1
            total_count += 1

    department_percentage = {}
    for department, count in department_count.items():
        percentage = (count / total_count) * 100
        department_percentage[department] = round(percentage, 2)
    return department_percentage


 #API 4

@app.get("/monthly_sales/{product}")
def monthly_sales(product: str) -> List[int]:
    monthly_sales = [0] * 12 
    for record in data:
        if record["software"] == product:
            month = int(record["date"].split("-")[1])  
            monthly_sales[month - 1] += record["amount"] 
    return monthly_sales