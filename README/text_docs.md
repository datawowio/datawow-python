### `datawow.texts` modules

# Table of Content
- [Category class](#category-class)
- [Closed Question class](#closed-question-class)
- [Conversation class](#conversation-class)

## Category class
Description: Classify type in many level of category type
```python
>>> from datawow.texts import CategoryClassify as cat
>>> result = cat('PROJECT KEY').create(params=param)
```

|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| conversation| array of dict|**Yes**| Example: `[{ "name": "...", "message": "..." }]`|
|title|string|**Yes**|Title of conversation|
|allow_empty |bool| |No|Answer can be empty|
|postback_url|string|No|URL for callback|
|postback_method| string|No| Configuration HTTP method GET POST PUT PATCH|
|custom_id| string|No| Custom ID that used for search|


## Closed Question class
Description: Classify inappropriate conversation
```python
>>> from datawow.texts import ClosedQuestion as close
>>> result = close('PROJECT KEY').create(params=param)
```

|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
|data|string|**Yes**|Stream of text to moderate|
|postback_url|string|No|URL for callback|
|postback_method| string|No| Configuration HTTP method GET POST PUT PATCH|
|custom_id| string|No| Custom ID that used for search|


## Conversation class
Description: Classify conversation
```python
>>> from datawow.texts import Conversation as conv
>>> result = conv('PROJECT KEY').create(params=param)
```

|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
|conversation| array of dict|**Yes**| Example: `["foo", "bar"]`|
|custom_conversation_ids|string|**Yes**|Example: `['1','2']`|
|postback_url|string|No|URL for callback|
|postback_method| string|No| Configuration HTTP method GET POST PUT PATCH|
|custom_id| string|No| Custom ID that used for search|



# Common function 
For every classes there are common functions to get list of data and find by ID. We've going to show you how to use it.

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
| image_id	     | string  |   **Yes** | Image's ID or custom ID which is you were assigned|
