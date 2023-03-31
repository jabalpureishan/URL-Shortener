import pyshorteners
import json
#requires the installation of pyshortener
class URLShortener:
    def __init__(self, filename='shortened_urls.json'):
        # Create an instance of the pyshorteners.Shortener class
        self.shortener = pyshorteners.Shortener()
        # Set the filename to save and load shortened URLs
        self.filename = filename
        # Load shortened URLs from file
        self.load_urls()

    def shorten_url(self, original_url):
        try:
            # Use the TinyURL service to shorten the URL
            short = self.shortener.tinyurl.short(original_url)
            # Save the shortened URL to file
            self.save_url(original_url, short)
            return short
        except Exception as e:
            print(f"Error: {e}")
            return None

    def restore_url(self, short):
        try:
            # Use the TinyURL service to expand the shortened URL
            original_url = self.shortener.tinyurl.expand(short)
            return original_url
        except Exception as e:
            print(f"Error: {e}")
            return None

    def save_url(self, original_url, short):
        # Load shortened URLs from file
        urls = self.load_urls()
        # Add the new shortened URL
        urls[original_url] = short
        # Save shortened URLs to file
        with open(self.filename, 'w') as f:
            json.dump(urls, f)

    def load_urls(self):
        try:
            # Load shortened URLs from file
            with open(self.filename, 'r') as f:
                urls = json.load(f)
                return urls
        except FileNotFoundError:
            # Return an empty dictionary if the file does not exist
            return {}

# Create an instance of the URLShortener class
url_shortener = URLShortener()
# Get the original URL from the user
original_url = input("Enter the URL to shorten: ")
# Shorten the URL using the shorten_url method
shortened_url = url_shortener.shorten_url(original_url)
if shortened_url:
    print(f"Shortened URL: {shortened_url}")
else:
    print("Failed to shorten URL")
# Restore the original URL using the restore_url method
restored_url = url_shortener.restore_url(shortened_url)
if restored_url:
    print(f"Restored URL: {restored_url}")
else:
    print("Failed to restore URL")
