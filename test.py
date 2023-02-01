# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests

model_inputs = {'input':["i loved the spiderman movie!", "pineapple on pizza is the worst 🤮"]}

res = requests.post('http://localhost:8000/', json = model_inputs)

print(res.json())
