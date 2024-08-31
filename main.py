import requests
from bs4 import BeautifulSoup as bs

# An empty list to store URLs
urls = []

# HTML snippets with follower and following counts
html = '''
<span class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs">348</span>
'''

html2 = '''
<span class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs">437</span>
'''

# Function to allow the user to add a username to the list
def scrape():
    insta_user = input("Enter your Instagram username: ")
    urls.append(f"https://www.instagram.com/{insta_user}/")

# Call the scrape function
scrape()

# This loop is just to demonstrate the parsing, not actual web scraping
for url in urls:
    print(f"Fetching data for URL: {url}")

    # Parsing followers count from the first HTML snippet
    soup_followers = bs(html, 'html.parser')
    followers_count = soup_followers.find('span', class_="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs")
    follower = followers_count.get_text() if followers_count else "Not found"

    # Parsing following count from the second HTML snippet
    soup_following = bs(html2, 'html.parser')
    following_count = soup_following.find('span', class_="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs")
    following = following_count.get_text() if following_count else "Not found"

    # Print extracted values
    print(f"Followers: {follower}")  # Output: 348
    print(f"Following: {following}")  # Output: 437

# ''' compare follower and following ratio '''

    try:
        follower_count = int(follower)
        following_count = int(following)

        # Example comparison or processing
        if follower_count > following_count:
            print("You have more followers than followings.")
        elif follower_count < following_count:
            print("You are following more people than you have followers.")
        else:
            print("Your followers and followings are equal.")
    
    except ValueError:
        print("Error converting follower/following counts to numbers.")
    