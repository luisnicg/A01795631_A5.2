"""The program computes the total cost."""

import sys
import os
import time
import json


def total_cost(filepath_product, filepath_sales):
    """Loads a file from a given filename.

    Args:
        filepath_product: The name of the file that contains the product.
        filepath_sales: The name of the file that contains the sales record.
    Returns:
      float: Total sales amount, or None if an error occurs
    """

    if not os.path.exists(filepath_product):
        print(f"Error: File '{filepath_product}' not found.")
        return

    if not os.path.exists(filepath_sales):
        print(f"Error: File '{filepath_sales}' not found.")
        return

    try:
        start_time = time.time()  # Getting start time

        # Print SalesResults.txt
        with open("SalesResults.txt", "w", encoding="utf-8") as outfile:
            with open(filepath_product, 'r', encoding="utf-8") as f:
                products = json.load(f)

            with open(filepath_sales, 'r', encoding="utf-8") as f:
                sales = json.load(f)

            #  Req 2
            total_sales = 0
            #  Req 6
            for sale in sales:  # Iterate through the list of sales records
                product_name = sale.get("Product")
                quantity = sale.get("Quantity")
                if not product_name or not quantity:
                    print("Invalid sales record. Skipping.")
                    continue  # Skip invalid records

                for product in products:
                    if product["title"] == product_name:
                        price = product.get('price')
                        if price:
                            total_sales += price * quantity
                            break
                        else:
                            print(f"Price not found for '{product_name}'.")
                            break
                else:
                    print(f"Product '{product_name}' not found.")

            #  Req 7
            end_time = time.time()  # Getting end time
            elapsed_time = end_time - start_time

            print("TOTAL")
            print(f"{filepath_sales[:3]}: {total_sales:.2f}")
            print(f"ELAPSED TIME: {elapsed_time:.4f} seconds")
            outfile.write("TOTAL\n")
            outfile.write(f"{filepath_sales[:3]}: {total_sales:.2f}\n")
            outfile.write(f"ELAPSED TIME: {elapsed_time:.4f} seconds\n")

    #  Req 3
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in one or both input files.")
        return None
    except Exception as e:
        print(f"Error: Something went wrong while reading the file: {e}")


#  Req 1
if __name__ == "__main__":
    if len(sys.argv) != 3:
        #  Req 5
        print("Usage: python computeSales.py <filename1> <filename2>")
    else:
        file_arg_1 = sys.argv[1]
        file_arg_2 = sys.argv[2]
        total_cost(file_arg_1, file_arg_2)
