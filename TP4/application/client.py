import requests
import json
import argparse
import sys

parser = argparse.ArgumentParser(
    description='Add new bill and get most frequent product')

parser.add_argument('--server', dest='server_url',
                    help='server url', default='localhost')

parser.add_argument('--port', dest='server_port',
                    help='port server url', default='5000')

parser.add_argument('--action', dest='action',
                    help='action to perform, ADD or MOST', default='ADD')


def post_request(server_url):
    print("Enter :q to quit without sending to server")
    print("Enter :wq to quit and send")

    SAVE_AND_QUIT = ":wq"
    QUIT = ":q"

    product_list = []

    while True:
        product_name = input("Product name: ")

        if product_name == SAVE_AND_QUIT:
            break
        elif product_name == QUIT:
            sys.exit(0)
        else:
            try:
                product_price = input("Product price (Double):")
                if product_price == SAVE_AND_QUIT:
                    break
                elif product_name == QUIT:
                    sys.exit(0)

                product_price = float(product_price)
            except Exception as e:
                print(e)
                raise Exception
        product_list.append(
            {"product_name": product_name, "price": product_price})

    if len(product_list) > 0:
        print(server_url)
        print(product_list)
        req = requests.post("http://localhost:5000/factures/", json={
                            "articles": product_list}, headers={"content-type": "application/json"})
        print(req.status_code)
    else:
        print("no product added")


def get_most_request(server_url):
    try:
        req = requests.get(server_url+"/most")
        res = req.json()
        print(json.dumps(
            sorted(res, key=lambda x: x['freq'], reverse=True), indent=4))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    args = parser.parse_args()

    server_url = args.server_url+":"+args.server_port

    if args.action == "ADD":
        post_request(server_url)
    elif args.action == "MOST":
        get_most_request(server_url)
    else:
        print("Illegal action --action ADD or --action MOST")
