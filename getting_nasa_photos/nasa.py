from aiohttp import web, ClientSession
from aiohttp.web import HTTPFound
from PIL import Image

import io
import random

# API key provided by NASA (you can use the default one: DEMO_KEY)
NASA_API_KEY = 'DEMO_KEY'
# Each rover has its own URL. For Curiosity it's https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos
ROVER_URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'


async def validate_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return image.width >= 1024 and image.height >= 1024 # and image.mode != 'L'  --> to reject greyscale images


async def get_mars_image_url_from_nasa():
    while True:
        # sol: the Martian rotation or day on which a photo was taken, counting up from the rover's landing date
        # (the maximum value can be found in rover/max_sol part of the response)
        # we select a random sol (for Curiosity the max_sol value is 1722 at the moment of writing this post)
        sol = random.randint(0, 1722)
        params = {'sol': sol, 'api_key': NASA_API_KEY}

        # ClientSession creates a session that we can use to get the response from NASA API
        # we obtain the JSON response using resp.json()
        async with ClientSession() as session:
            async with session.get(ROVER_URL, params=params) as resp:
                resp_dict = await resp.json()

        # we check if the 'photos' key is present in the response; if not, we have reached the limit of hourly
        # calls and we need to wait a bit
        if 'photos' not in resp_dict:
            raise Exception

        photos = resp_dict['photos']
        print(resp_dict)

        # if there are no photos taken on given day, we check again, for a different random sol
        if not photos:
            continue

        return random.choice(photos)['img_src']


async def get_mars_photo_bytes():
    while True:
        # we get the URL using the previously defined function and we read the raw bytes from
        # the image using resp.read()
        image_url = await get_mars_image_url_from_nasa()
        async with ClientSession() as session:
            async with session.get(image_url) as resp:
                image_bytes = await resp.read()
        # we check if our image is good enough; if not, we keep looking
        if await validate_image(image_bytes):
            break
    return image_bytes


async def get_mars_photo(request):
    # get_mars_photo coroutine is a request handler; it takes a HTTP request as its only
    # argument and is responsible for returning a HTTP response (or raising an exception)

    image = await get_mars_photo_bytes()

    # once we have a satisfying photo we put it in the response (notice we still use the same web.Response
    # as before, but this time we specify the body instead of text and we define the content_type)
    return web.Response(body=image, content_type='image/jpeg')



# Note: request handlers don't have to be coroutines, they can be regular functions.
# But we are going to use the power of asyncio, so most functions in our program are going
# to be defined with async def


# app is a high level server; it supports routers, middleware and signals
# (for this program we are only going to use the router)
app = web.Application()
# app.router.add_get registers a request handler on HTTP GET method and '/' path
app.router.add_get('/', get_mars_photo, name="mars_photo")


# To run the application
web.run_app(app, host='127.0.0.1', port=8080)
# Or use aiohttp-devtools
# pip install aiohttp-devtools
# adev runserver -p 8080 nasa.py
