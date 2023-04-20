import requests
import json
import time
import random

# Lista sistemelor SAP pentru echilibrarea încărcăturii
sisteme = [
    {
        "id_sistem": "sistem1",
        "base_url": "https://sistem1.example.com",
        "max_concurrent_requests": 10,
        "current_requests": 0,
        "last_request_time": 0,
        "load_limit": 100,
        "timeout": 5
    },
    {
        "id_sistem": "sistem2",
        "base_url": "https://sistem2.example.com",
        "max_concurrent_requests": 10,
        "current_requests": 0,
        "last_request_time": 0,
        "load_limit": 200,
        "timeout": 10
    }
]

# Funcția pentru a obține sistemul cu cea mai mică încărcătură
def get_system_with_lowest_load():
    lowest_load_system = None
    for system in sisteme:
        if lowest_load_system is None or \
                system["current_requests"] < lowest_load_system["current_requests"]:
            lowest_load_system = system
    return lowest_load_system

# Funcția pentru a trimite o solicitare către sistemul SAP
def send_request(system):
    system["current_requests"] += 1
    system["last_request_time"] = time.time()
    response = requests.get(system["base_url"], timeout=system["timeout"])
    system["current_requests"] -= 1
    return response

# Funcția pentru echilibrarea încărcăturii între sistemele SAP
def balance_load():
    system = get_system_with_lowest_load()
    if system is not None:
        if system["current_requests"] < system["max_concurrent_requests"]:
            response = send_request(system)
            return response

# Exemplu de utilizare a funcției de echilibrare a încărcăturii
for i in range(100):
    response = balance_load()
    if response is not None:
        print(response.status_code)
    else:
        print("Nu există sisteme SAP disponibile pentru a procesa solicitarea")
