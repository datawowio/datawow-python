###  `datawow.videos` modules

# Table of Content
- [Video classify class](#video-classify-class)

## Video classify class
Description: Video classification

### Create
```python
>>> from datawow.videos import VideoClassify as video
>>> result = video('PROJECT KEY').create(params=param)
```

#### params
| Field        | Type           | Required  | Description |
| ------------- |:-------------:| :-----:| :-----|
| data     | 	string | **Yes** |URL of Video|
| play_at | float |No |Setting video start time|
| allow_seeking |bool| No |Allow seeking video player (default `true`)|
|muted |bool|No| Mute video on start (default: `true`)|
| postback_url	     | string      | No | URL for answer callback once video has been checked|
| postback_method     | 	string | No |Configuration HTTP method GET POST PUT PATCH|
| custom_id	     | string      |   No |Custom ID that used for search|


# Common function 
For every class there common function to get list of data and find by ID which we've going to show you how to use is.

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
