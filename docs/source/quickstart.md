# Quickstart

## Installation

Install the Lagoon package for python

```python
python -m pip install lagoon-python-api
```
OU
```python
python -m pip install git+https://github.com/fatfish-lab/lagoon-python-api.git
```

## Get your organisations

All Lagoon's data are segmented by organisations. You can get all the organisations you have access to by using the following code:

```python
from lagoon import Lagoon

lg=Lagoon('https://your-lagoon-server')
lg.signin(LG_USER, LG_PASSWORD)

organisations = lg.get_organisations()
organisation = organisations[0]

```

You can also signin to Lagoon using a bot:

```python
from lagoon import Lagoon

lg=Lagoon('https://your-lagoon-server')
lg.bot(LG_BOT_KEY).signin(LG_BOT_SECRET)
```

Once you have access to an organisation, you can get all the talents, hardware and licenses of this organisation:

```python
talents = organisation.get_talents()
hardware = organisation.get_hardware()
licenses = organisation.get_licenses()
```

Learn more in the reference documentation. Feel free to reach us at [support@fatfi.sh](mailto:support@fatfi.sh)