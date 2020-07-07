"""
li = "Bangladesh", "nepal", "India", "Srilanka"
print([item.capitalize() for item in li if item.lower().endswith("a") or item.lower().endswith("h")])

"""

import re
s = "Afganistan, America, bangladesh, Canada, denmark, England, Netherlands, New Zealand, Sweden, Switzerland"
li = re.findall(r'(\w+lands*)', s)
print(li)