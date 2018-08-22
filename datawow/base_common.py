def base_url(model):

    url = {
        "images": "https://k-sequencing.datawow.io/",
        "ai": "https://k-sequencing.datawow.io/",
        "texts": "https://kiyo-text.datawow.io/",
        "videos": "https://k-sequencing.datawow.io/"
    }

    return url.get(model, 'Not found')
