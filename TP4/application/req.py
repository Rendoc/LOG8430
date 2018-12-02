import requests


r = requests.post("http://127.0.0.1:5000/factures/", json={"title": "Roger Gaudry", "total": 21.00, "articles": [
                  {"id": 1, "name": "banane", "qty": 12,
                      "unit_price": 1.00, "product_price_total": 12.00},
                  {"id": 2, "name": "Orange", "qty": 3,
                      "unit_price": 3.00, "product_price_total": 9.00}]})


r = requests.post("http://127.0.0.1:5000/factures/", json={"title": "IGA", "total": 16.00, "articles": [
                  {"id": 3, "name": "peche", "qty": 3,
                      "unit_price": 4.00, "product_price_total": 12.00},
                  {"id": 2, "name": "Kitkat", "qty": 4,
                      "unit_price": 1.00, "product_price_total": 4.00}]})


r = requests.post("http://127.0.0.1:5000/factures/", json={"title": "Metro", "total": 12.00, "articles": [
                  {"id": 1, "name": "banane", "qty": 24,
                      "unit_price": 0.50, "product_price_total": 12.00},
                  ]})
