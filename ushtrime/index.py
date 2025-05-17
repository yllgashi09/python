data = {
    "name" : "John doe",
    "age": 30,
    "address": {
        "street": "123 street",
        "city": "prishtina"
    },
    "contact": [
        {
            "type": "email"
        },
        {
            "type": "email"
        },
        {
            "type": "phone"
        }
    ]
}
print(data["contact"][1]["type"])