#!/usr/bin/env python3
# -*- coding: utf-8 -*- Line 2
# ----------------------------------------------------------------------------
# Created By  : Marco Rabelink
# Created Date: 18/10/2022
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Ansible Automation Platform Certified Collections List Download
This can be used to download collections and use the downloaded collections
to import in an on-premise automation-hub that not has internet connection.
"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from asyncio import subprocess
import requests
import subprocess
from bs4 import BeautifulSoup

# Get certified content webpage
url = "https://access.redhat.com/articles/3642632"
data = requests.get(url).text

# Creating BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')

# Find the table with certified content in ansible automation hub
table = soup.find("table")
download = list()

# Get all links in table and if . is in string text
# append in download list.
for row in table.findAll("a", href=True):
    if '.' in row.text:
        download.append(row.text)

# Download the list using ansible-galaxy
# Needs ansible 2.12 >= for ansible-galaxy collection download option
for collection in download:
    p = subprocess.Popen(
        f"ansible-galaxy collection download {collection}", stdout=subprocess.PIPE, shell=True)
    print(p.communicate())
