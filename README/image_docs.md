### `datawow.images` modules

# Table of Content

- [Choice class](#choice-class)
- [Closed Question class](#closed-question-class)
- [Image message class](#image-messages-class)
- [Photo tags class](#photo-tags-class)

---
## Choice class
Description: Yes or No Question from Image

### Create
```python
>>> from datawow.images import Choice as choice
>>> result = choice('PROJECT KEY').create(params=param)
```
#### params 

|Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| instruction| string|**Yes**| Tell moderator what answer you expected and what image is|
|categories | Array[string]|**Yes** | List of answers that you were expected. sparate by use space |
| data |string | **Yes** |URL of image|
| postback_url| string|No| URL for answer callback once image has been checked|
| postback_method|string | No |Configuration HTTP method GET POST PUT PATCH|
| allow_empty| boolean|No|Allow answer can be blank. default is `false`|
|multiple | boolean | No | Configuration for multiple selection of category to answer default is `false` |
| custom_id | string | No |Custom ID that used for search|


## Closed Question class
Description: Standard Criteria

### Create
```python
>>> from datawow.images import ClosedQuestion as closed
>>> result = closed('PROJECT KEY').create(params=param)
```
#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| data     | 	string | **Yes** |URL of image|
| postback_url	     | string      | No | URL for answer callback once image has been checked|
| postback_method     | 	string | No |Configuration HTTP method GET POST PUT PATCH|
| custom_id	     | string      |   No |Custom ID that used for search|


## Image messages class
Description: Message Question from Image

### Create
```python
>>> from datawow.images import Message as message
>>> result = message("PROJECT KEY").create(params=param)
```

#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| instruction	     | string      |   **Yes** | Tell moderator what answer you expected and what image is|
| data     | 	string | **Yes** |URL of image|
| postback_url	     | string      | No | URL for answer callback once image has been checked|
| postback_method     | 	string | No |Configuration HTTP method GET POST PUT PATCH|
| custom_id	     | string      |   No |Custom ID that used for search|



## Photo tags class
Description: Tag an object in the image

### Create
```python
>>> from datawow.images import PhotoTag as photo_tag
>>> result = photo_tag("PROJECT KEY").create(params=param)
```

#### params
| Field | Type| Required | Description |
| ------------- |:-------------:| :-----:| :-----|
|instruction| string|**Yes** |Tell moderator what answer you expected and what image is|
|data|string| **Yes** |URL of image|
|postback_url|string| No |URL for answer callback once image has been checked|
|postback_method|string | No |Configuration HTTP method GET POST PUT PATCH|
|custom_id|string|No|Custom ID that used for search|



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

