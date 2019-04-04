def base_url(model):

    url = {
        "images": "https://image.datawow.io/api/v1/",
        "videos": "https://image.datawow.io/api/v1/",
        "texts":  "https://text.datawow.io/api/v1/",
        "ai":     "https://image.datawow.io/api/v1/",
        "docs":   "https://image.datawow.io/api/v1/",
        "consensus": "https://image.datawow.io/api/v1"
    }

    return url.get(model, 'Not found')
