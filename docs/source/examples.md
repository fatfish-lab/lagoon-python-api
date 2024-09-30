# Examples

Here is some examples to perform specific actions. Feel free to look directly at the classes documentation to know the parameters you can use as well as the functions available.

## Get all organisations

```python
organisations=lg.get_organisations()
```

## Get talents, hardware and licenses of an organisation
```python
organisation=organisations[0]

talents=organisation.get_talents()
hardware=organisation.get_hardware()
licenses=organisation.get_licenses()
```

## Generate a product barcode

```python
products=organisation.get_products()
product=products[0]
product.save_barcode('/path/to/folder/')
```

## Signin to Lagoon with a bot

```python
from lagoon import Lagoon

lg=Lagoon('https://your-lagoon-server')
lg.bot(LG_BOT_KEY).signin(LG_BOT_SECRET)
```