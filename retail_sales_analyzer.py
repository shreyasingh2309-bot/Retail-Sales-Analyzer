#  Creating Retail Sales Dataset

sales_data = [
    {"Product": "Laptop", "Category": "Electronics", "Quantity": 5, "Price": 45000},
    {"Product": "Mobile", "Category": "Electronics", "Quantity": 10, "Price": 15000},
    {"Product": "Headphones", "Category": "Electronics", "Quantity": 15, "Price": 2000},
    {"Product": "Chair", "Category": "Furniture", "Quantity": 8, "Price": 3000},
    {"Product": "Table", "Category": "Furniture", "Quantity": 4, "Price": 7000},
    {"Product": "Shoes", "Category": "Fashion", "Quantity": 12, "Price": 2500},
    {"Product": "Watch", "Category": "Fashion", "Quantity": 7, "Price": 4000},
    {"Product": "Bag", "Category": "Fashion", "Quantity": 9, "Price": 1800}
]

#  Calculate Revenue

for item in sales_data:
    item["Revenue"] = item["Quantity"] * item["Price"]

#  Display Sales Records

print(" RETAIL SALES ANALYZER ")
print("PRODUCT SALES RECORDS")

for item in sales_data:
    print(item["Product"], "| Quantity:", item["Quantity"],
          "| Revenue: Rs.", item["Revenue"])

# Overall Sales Analysis

total_revenue = sum(item["Revenue"] for item in sales_data)
total_quantity = sum(item["Quantity"] for item in sales_data)
total_transactions = len(sales_data)

average_revenue = total_revenue / total_transactions

print("\n========== SALES SUMMARY ==========")
print("Total Revenue: Rs.", total_revenue)
print("Total Quantity Sold:", total_quantity)
print("Total Transactions:", total_transactions)
print("Average Revenue: Rs.", round(average_revenue, 2))

#  Product-Wise Analysis

product_revenue = {}
product_quantity = {}

for item in sales_data:
    product = item["Product"]

    product_revenue[product] = product_revenue.get(product, 0) + item["Revenue"]
    product_quantity[product] = product_quantity.get(product, 0) + item["Quantity"]

best_selling_product = max(product_quantity, key=product_quantity.get)
highest_revenue_product = max(product_revenue, key=product_revenue.get)

print(" PRODUCT ANALYSIS ")
print("Best Selling Product:", best_selling_product)
print("Highest Revenue Product:", highest_revenue_product)

#  Category-Wise Analysis

category_revenue = {}

for item in sales_data:
    category = item["Category"]

    category_revenue[category] = category_revenue.get(category, 0) + item["Revenue"]

print(" CATEGORY ANALYSIS ")

for category, revenue in category_revenue.items():
    print(category, ": Rs.", revenue)

top_category = max(category_revenue, key=category_revenue.get)

print("Top Performing Category:", top_category)

# Sales Performance Classification

print(" SALES PERFORMANCE ")

for item in sales_data:
    if item["Revenue"] >= 20000:
        status = "High Sales"
    else:
        status = "Low Sales"

    print(item["Product"], ":", status)

# Sales Target Analysis

sales_target = 300000

print(" TARGET ANALYSIS ")
print("Sales Target: Rs.", sales_target)
print("Actual Revenue: Rs.", total_revenue)

if total_revenue >= sales_target:
    print("Sales Target Achieved!")
else:
    print("Sales Target Not Achieved!")

# Final Business Insights

print(" FINAL BUSINESS INSIGHTS ")
print("Total Revenue: Rs.", total_revenue)
print("Best Selling Product:", best_selling_product)
print("Highest Revenue Product:", highest_revenue_product)
print("Top Performing Category:", top_category)

