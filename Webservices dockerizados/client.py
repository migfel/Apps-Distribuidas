import requests

def main():
    quantity = int(input('Enter quantity: '))
    product_name = input('Enter product name: ')
    price = float(input('Enter price: '))

    payload = {
        'quantity': quantity,
        'product_name': product_name,
        'price': price
    }

    response = requests.post('http://localhost:5000/process_sale', data=payload)

    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)

if __name__ == '__main__':
    main()
