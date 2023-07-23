# InstaPhoto

FastAPI/Selenium backend for get photos from Instagram

Both method returns photo_counts of ulrs

1. GET /getPhotos/{username}?max_count={photo_counts}
   Using side service and Selenium to get photo of instagram user username
   max_count is optional.

2. GET /getPhotosDummy/{username}?max_count={photo_counts}
   Using side service and BS4 to get photo of instagram user username
   max_count is optional.
