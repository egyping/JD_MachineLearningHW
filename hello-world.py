convos_one = [
    {
        "customer": "Hi there, what time do you open tomorrow for lunch?",
        "tags": ["opening", "closing", "hours"],
    },
     {
        "customer": "Can I speak to your manager?",
        "tags": ["customer_support"],
    },
    {
        "customer": "The food was amazing thank you!",
        "tags": ["customer_support", "feedback"],
    },
     {
      "customer": "What type of products do you have?",
       "tags": ["products", "menu", "inventory", "food"],
    }  
    
]



convos_two = [
    {
        "customer": "How late is your kitchen open?",
        "tags": ["opening", "hours", "closing"],
    },
     {
        "customer": "My order was prepared incorrectly, how can I get this fixed?",
        "tags": ["customer_support"],
    },
    {
        "customer": "What kind of meats do you have?",
        "tags": ["menu", "products", "inventory", "food"],
    }
]



convos_three = [
    {
        "customer": "When does your dining room open?",
        "tags": ['opening', 'hours'],
    },
     {
        "customer": "When do you open for dinner?",
        "tags": ['opening', 'hours', "closing"],
    },
    {
        "customer": "How do I contact you?",
        "tags": ["contact", "customer_support"]
    }
]

dataset = convos_one + convos_two + convos_three
print(dataset)