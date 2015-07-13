ObjectRocket Python Client
==========================
ObjectRocket API bindings for Python.


### examples
To use the bindings, simply do the following:


```python
import objectrocket
>>>

client = objectrocket.Client('<username>', '<password>')
>>>

# create a new instance
client.instances.create(name='instance0', size=5, zone='US-West'
>>> <MongodbInstance {...} at 0x10aedb990>

# get an instances object
client.instances.get('instance0')
>>> <MongodbInstance {...} at 0x10aedb980>

# get all instances
client.instances.all()
>>> [<MongodbInstance {...} at 0x10aedb980>]
```


### installation

    pip install objectrocket


### development
#### test
Before you push your code, run `tox` from the top level directory. If errors
are reported, fix them.

#### coverage
To receive a test coverage report, run `tox -e coverage` from the top level directory.

#### build
To build the client, invoke `tox -e build` from the top level directory.
Your artifact will appear in the `dist` directory, and will look
something like `objectrocket-<version>-py2.py3-<abi>-<platform>.whl`.

#### documentation
To build the documentation, invoke `tox -e docs` from the top level directory.
The HTML index can then be found at `docs/build/html/index.html`.
