"""
Copyright GRIJP, Jean.
"""

import requests
###############################################################################




url = "https://www.duolingo.com"
res = requests.get(url)
texto = res.text
print(texto)