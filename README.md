# Datawow-python
HTTP RESTFul for calling DataWow APIs 
###### support or question support@datawow.io

# Installation 
```
pip install datawow
```
or
```
pip2 install datawow
```

The library has supports following version of python:

* Python 2.7 tested
* Python 3.5 tested
* Python 3.6 tested  

**Recommendation:**  We've created virtual-env for Python 3.5 on development process, thus we recommended to use Python version 3.5 or above. 

For user who use **conda**, we haven't contribute yet


# Usage


## Import 
```python
>>> import datawow as ks
```
 There are 4 modules for API that you can import into your system
 
1. Image API module
```python
>>> import datawow.images as ks
``` 
2. Text API module
```python
>>> import datawow.texts as ks
``` 

3. Video API module
```python
>>> import datawow.videos as ks
``` 

4. AI/Prediction API module
```python
>>> import datawow.predictions as ks
``` 


## Functions explanation 
### `datawow.images` module
In the image module, there are 4 APIs

```python
>>> ks.Choice()
>>> ks.Message()
>>> ks.PhotoTag()
>>> ks.ClosedQuestion()
``` 
---
### `datawow.videos` module
In the video module, there are 1 APIs

```python
>>> ks.VideoClassify()
``` 
---
### `datawow.texts` module
In the text module, there are 3 APIs

```python
>>> ks.CategoryClassify()
>>> ks.Conversation()
>>> ks.ClosedQuestion()
``` 
---
### `datawow.predictions` module
In the prediction module, there are 1 APIs

```python
>>> ks.Predictor()
``` 

# Demo and Usage
 - Image Documentation [link](README/image_docs.md)
 - Video Documentation [link](README/video_docs.md)
 - Text Documentation [link](README/text_docs.md)
 - AI/Prediction Documentation [link](README/ai_docs.md)


## Working with response
### `datawow.responses` module
To use response which is data has been contained in `response` class and you can use dot operation to get you data 

```python 
>>> result.data
```
For check error or status by calling this 

```python 
>>> result.error_code # 401
>>> result.message # Not authenticated
```

also you can check HTTP success by following

```python 
>>> result.code # 200
```

To use meta data such as pagination

```python 
>>> result.meta # {'code': 200, 'message': 'success'}
```
