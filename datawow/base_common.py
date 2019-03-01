def base_url(model):

    url = {
        "images": "https://kiyo-image.datawow.io/",
        "videos": "https://kiyo-image.datawow.io/",
        "texts":  "https://kiyo-text.datawow.io/",
        "ai":     "https://kiyo-image.datawow.io/",
        "docs":   "https://kiyo-image.datawow.io/"
    }

    return url.get(model, 'Not found')
