import requests

base_url = "https://parsel-selector-api.herokuapp.com"

params = {
    "url": f"{base_url}/examples/html",
    "path": "<span><strong>.*:<\/strong> (.*)<\/span>",
    "path_type": "REGEX",
}

# Example using BASIC return style
params["return_style"] = "BASIC"
r = requests.get(base_url, params=params)
print(r.json(), "\n")

# Example using DATA_ONLY return style
params["return_style"] = "DATA_ONLY"
r = requests.get(base_url, params=params)
print(r.text, "\n")

# Example using VERBOSE return style
params["return_style"] = "VERBOSE"
r = requests.get(base_url, params=params)
print(r.json(), "\n")
