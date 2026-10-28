import requests

# Faz a requisição HTTP à API pública do GitHub
response = requests.get("https://api.github.com/users/LeunamGuilherme")

if response.status_code == 200:
    data = response.json()
    print(f"User: {data['login']}")
    print(f"Public Repos: {data['public_repos']}")
else:
    print(f"Error fetching data. Status code: {response.status_code}")