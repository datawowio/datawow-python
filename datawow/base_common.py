def base_url(model):

    url = {
        "images": "https://kiyo-image.datawow.io/api/v1/",
        "videos": "https://kiyo-image.datawow.io/api/v1/",
        "texts":  "https://kiyo-text.datawow.io/api/v1/",
        "ai":     "https://kiyo-image.datawow.io/api/v1/",
        "docs":   "https://kiyo-image.datawow.io/api/v1/"
    }

    return url.get(model, 'Not found')
