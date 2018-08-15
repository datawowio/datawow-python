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

Python supports the following Python versions:

* Python 2.7 tested
* Python 3.5 tested
* Python 3.6 tested  

**Recommendation:**  We've created virtual-env for Python 3.5 on development process, thus recommended to use Python version 3.5 or later. 

For user who use **conda**, we haven't contribute yet


# Usage


## Import 
```python
>>> import datawow as ks
```
 There are 4 modules for API that you can specific the module as your expected 
 
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
In the image module, we have 4 APIs

```python
>>> ks.Choice()
>>> ks.Message()
>>> ks.PhotoTag()
>>> ks.ClosedQuestion()
``` 
---
### `datawow.videos` module
In the video module, we have 1 APIs

```python
>>> ks.VideoClassify()
``` 
---
### `datawow.texts` module
In the text module, we have 3 APIs

```python
>>> ks.CategoryClassify()
>>> ks.Conversation()
>>> ks.ClosedQuestion()
``` 
---
### `datawow.predictions` module
In the prediction module, we have 1 APIs

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
To get response that data has been contained in response class you can call them by name for example
```python 
>>> result.data
```
Data it's Dict you can do as you want like a JSON object

For check error or status by calling this 

```python 
>>> result.error_code # 401
>>> result.message # Not authenticated
```

also you can get HTTP success by this

```python 
>>> result.code # 200
```

To get meta data such as pagination

```python 
>>> result.meta # {'code': 200, 'message': 'success'}
```
