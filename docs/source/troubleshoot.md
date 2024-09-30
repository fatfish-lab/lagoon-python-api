# Troubleshoot

## Logging

To help you debug your application, or send information to support, we have set up logging within the Lagoon package.

Inside your tool, you can add the following lines of code:

```python
import logging

logging.basicConfig() # Initialize logging
lg_logger=logging.getLogger('lagoon') # Get the lagoon's package logger
lg_logger.propagate=True # Enable logger propagation
lg_logger.setLevel(logging.DEBUG) # Set the level of logging on DEBUG
```

## How can I check a class ?

To check if you are using an Item() or an Edge(), you can directly print the variable. If your variable is an instance of a class, the following output should appear, indicating the class name in parentheses as well as the data of the item or edge.
```python
print(group)
> (Group) {   '_id': 'items/1234',
            '_key': '1234',
            '_rev_: 'b234553',
            'type': 'Group',
            'data': {
                'name': 'My group'
            },
            'createdBy': '567',
            'updatedBy': '567',
            'createdAt': '2017-1...8.580Z',
            'updatedAt': '2017-1...8.580Z'}
```
