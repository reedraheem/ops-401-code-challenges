#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: TODO: Code Challenge 20
# Date:        TODO: August 30,2023
# Modified by: TODO: Raheem Sharif Reed

### TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
###The purpose of the given function, get_all_forms(url), is to retrieve all the HTML form elements present on a web page specified by the input url. In the context of the overall objectives of the script, this function serves the purpose of web scraping and data extraction. It uses the Beautiful Soup library to parse the HTML content of the webpage retrieved using the requests library, and then it searches for and collects all the <form> elements within the HTML content.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
###Overall, the function aids in the script's objective of understanding and interacting with web forms in a programmatic manner, potentially for automating data submission, testing form behavior, or extracting information from forms on web pages.
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
###Overall, this function plays a crucial role in the script's objective of testing for XSS vulnerabilities. It emulates the submission of a form with specific data, which includes a JavaScript payload, and retrieves the server's response. This enables the script to determine if the payload executed successfully and if the target URL is vulnerable to XSS attacks.
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
###In summary, the function serves the main purpose of scanning a given URL for XSS vulnerabilities by analyzing the forms present on the webpage, injecting a JavaScript payload, submitting the forms, and determining if the payload execution is successful. The function aims to provide information to the user about the presence of XSS vulnerabilities on the specified webpage.
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = """
    // TODO: Add HTTP and JS code here that will cause an XSS-vulnerable field to create an alert prompt with some text.
    """
    is_vulnerable = False
    
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    
    return is_vulnerable

# Main

### TODO: Add main explanation here ###
### In your own words, describe the purpose of this main as it relates to the overall objectives of the script ###
###The purpose of the main section, which is enclosed by the if __name__ == "__main__": condition, is to provide an entry point for executing the script's functionality. It interacts with the user, taking a URL as input and then calling a function named scan_xss(url) to test the entered URL for Cross-Site Scripting (XSS) vulnerabilities.
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection


