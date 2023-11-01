import requests

product_id = input("Enter Product Id for delete product:")

try:
    product_id = int(product_id)

except:
    product_id = None
    print("product_id is not valid id.")

if product_id:
    end_point = f"http://localhost:8000/api/product/{product_id}/delete/" 

    get_response = requests.delete(end_point)
    print(get_response.status_code, get_response.status_code==204)



# end_point = "http://localhost:8000/api/product/10/delete/" 


# get_response = requests.delete(end_point) 
# print(get_response.status_code, get_response.status_code==204)