from openai import OpenAI
from dotenv import load_dotenv
import os
import re

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

method_code = """
```python
# Code of the method (and class if needed)
def calculate_discount(price, discount_rate):
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount rate must be between 0 and 1.")
    return price * (1 - discount_rate)
```"""


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful coding assistant. Expected output format: (val1_value, val2_value). Provide only the output in the specified format. Do not add any additional text or explanation."},
        {
            "role": "user",
            "content": f"""Generate parameter input values for the following Python method to be used for unit testing. The values are to be used in tests that should cover typical use cases, edge cases, and error conditions.
                            {method_code}"""
        }
    ]
)

print(completion.choices[0].message)

# parse output
# Regular expression to match values inside parentheses
matches = re.findall(r'\((.*?)\)', completion.choices[0].message.content)

# Convert each match (a string) into a tuple of values
result = [tuple(map(eval, match.split(','))) for match in matches]

print(result)