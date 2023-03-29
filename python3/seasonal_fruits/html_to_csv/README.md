
# What is this?

It's a script that scrapes a webpage from WSU for agricultural data, and then outputs a CSV of harvesting seasons for various produce.

# How do I run this?

You need python3 installed, and then (from this directory) run:

```
mkdir venv
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
./convert.py > ../data.csv
deactivate
```

