### `datawow.documents` modules

# Table of Content

- [Document Verification class](#document-verification-class)

---
## Document Verification class
Description: Simple function to verify card's data

### Create
```python
>>> from datawow.document import Verification as verify
>>> result = verify('PROJECT KEY').create(params=param)
```
#### params 

|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| data |string | **Yes** |URL of image|
| postback_url| string|No| URL for answer callback once image has been checked|
| postback_method|string | No |Configuration HTTP method GET POST PUT PATCH|
| custom_id | string | No |Custom ID that used for search|

# Common function
For every classes there are common functions to get list of data and find by ID. We're going to show you how to use it.

## Query list of data by  `list()`

```python 
>>> from datawow.[some_model] import [the_model] as model
>>> result = model("PROJECT KEY").list()
```
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| page     | 	interger | No | default 0|
| per_page 	     | string      | No | default 20 |


## Find data with ID by  `find_id()`
```python
>>> from datawow.[some_model] import [the_model] as model
>>> result = model("PROJECT KEY").find_id("YOUR IMAGE ID")
```
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :----:| :-----|
| doc_id	     | string  |   **Yes** | Image's ID or custom ID which is you were assigned|
