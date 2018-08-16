### `datawow.predictions` modules


# Table of Content
- [How to use it](#create)
## [Type of AI](#response-of-each-type-ai)
- [Standard Criteria](#standard-criteria)
- [Nudity/Sexual](#nuditysexual)
- [Demographic](#demographic)
- [Standard Criteria & Human](#standard-criteria--human)

## Images (AI Beta)

- Standard Criteria
- Nudity/Sexual
- Demographic
- Standard Criteria & Human

### Create
```python
>>> from datawow.predictions import Predictor as predict
>>> result = predict("PROJECT KEY").create(params=param)
```
##### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| data     | 	string | Yes |Data for attachment|
| postback_url	     | string      | No | Image postback url|
| postback_method     | 	string | No |Postback method|
| custom_id	     | string      |   No |Custom's id|



### Response of each type AI
There are a difference type of response AI module here is a compare response of each
#### Standard Criteria
```python 
"""
{ 
  'image': { 'answer': 'approved',
  'credit_charged': 0,
  'custom_id': None,
  'data': '[image URL]',
  'id': '5a570d8860f4f17a353d313b',
  'postback_url': '[your callback URL]',
  'processed_at': None,
  'project_id': 87,
  'status': 'processing'}
}
"""
```
#### Nudity/Sexual
```python
"""
{ 
  'image': { 'answer': { 'sexual': 0.0003511860850267112 } ,
  'credit_charged': 1,
  'custom_id': None,
  'data': '[image URL]',
  'id': '5a547c1660f4f17a353d310c',
  'postback_url': '[your URL]',
  'processed_at': '2018-01-11T11:53:15.197+07:00',
  'project_id': 81,
  'status': 'processed'}
}
"""
```
#### Demographic
```python
"""
{ 
  'data': { 'answer': { 'result': [ 
   { 'age': 25,
     'age_prob': 0.08679278939962387,
     'gender': 'male',
     'gender_prob': 0.9268079400062561,
     'positions': 
	    {  'h': 268.20000000000005,
           'w': 248.8,
           'x': 0,
           'y': 11.599999999999994
        }
     }
 ]},
  'credit_charged': 0,
  'custom_id': None,
  'data': '[image URL]',
  'id': '5a5706f460f4f17a353d313a',
  'postback_url': '[your callback URL]',
  'processed_at': '2018-01-11T13:40:57.789+07:00',
  'project_id': 80,
  'status': 'processed'}
}
"""
```
#### Standard Criteria & Human
```python
"""
{
  'data': { 'image': { 'answer': 'approved',
  'credit_charged': 1,
  'custom_id': None,
  'data': '[image URL]',
  'id': '5a547c1660f4f17a353d310c',
  'postback_url': '[your URL]',
  'processed_at': '2018-01-11T11:53:15.197+07:00',
  'project_id': 81,
  'status': 'processed'}}
}
"""
```



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
