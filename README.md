# InstaPhoto

FastAPI/Selenium backend for get photos from Instagram

Both method returns _photo_counts_ of ulrs in format:

```
{
   urls: [
         "https://...",
         "https://...",
         "https://...",
      ]
}
```

### Start service

#### Local

```
pip install -r requirements.txt
python main.py
```

#### Docker

```
cd docker
docker-compose up
```

### Using Instagram WebUI:

1. `GET /getPhotos/{username}?max_count={photo_counts}`

   Using _Instagram WebUI_ and _Selenium_ to get _photo_counts_ of photos of instagram user _username_. _photo_counts_ is optional parameter, by default return all.

   **Important!** For using this method is necessary to add valid instagram login and password to _login.json_.

   ```
   {
      "username": "YOUR LOGIN/EMAIL",
      "password": "YOUR PASSWORD"
   }
   ```

### Using Side service:

2. `GET /getPhotosSide/{username}?max_count={photo_counts}`

   Using _Side service_ web interface and _Selenium_ to get _photo_counts_ of photos of instagram user _username_. _photo_counts_ is optional parameter, by default return all.

3. `GET /getPhotosBS/{username}?max_count={photo_counts}`

   Using HTTP request to _side service_ and _BS4_ to get _photo_counts_ of photos of instagram user _username_. _photo_counts_ is optional parameter, by default return all.
