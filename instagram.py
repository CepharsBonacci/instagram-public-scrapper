import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login (optional)
# If you want to scrape private profiles, you need to provide login credentials
# loader.login("your_username", "your_password")

# Scrape the "username" Instagram profile
profile = instaloader.Profile.from_username(loader.context, "username")

# Iterate over the profile's posts and download the photos
for post in profile.get_posts():
    loader.download_post(post, target=f"{profile.username}/{post.date_utc}")

