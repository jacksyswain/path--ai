import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

data = response.json()

user = data["results"][0]

print("Name:", user["name"]["first"])
print("Email:", user["email"])
print("Country:", user["location"]["country"])
print("Name:", user["name"]["first"])
print("Email:", user["email"])
print("Country:", user["location"]["country"])