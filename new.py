import requests
from bs4 import BeautifulSoup as bs

# HTML snippets with follower and following counts for demonstration purposes
html = '''
<span class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs">348</span>
'''

html2 = '''
<span class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs">437</span>
'''

# Function to scrape follower and following counts
def scrape(username):
    url = f"https://www.instagram.com/{username}/"
    # For demonstration purposes, we'll assume the HTML response is loaded in `html` and `html2`.
    # In real web scraping, you would fetch and parse this dynamically.

    # Parsing followers count from the first HTML snippet
    soup_followers = bs(html, 'html.parser')
    followers_count = soup_followers.find('span', class_="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs")
    follower = followers_count.get_text() if followers_count else "Not found"

    # Parsing following count from the second HTML snippet
    soup_following = bs(html2, 'html.parser')
    following_count = soup_following.find('span', class_="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs")
    following = following_count.get_text() if following_count else "Not found"

    # Print extracted values
    print(f"Username: {username}")
    print(f"Followers: {follower}")
    print(f"Following: {following}")

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

        # Calculate ratio
        result = ratio(follower_count, following_count)
        print("The followers vs following ratio is: ", result)

    except ValueError:
        print("Error converting follower/following counts to numbers.")

# Function to calculate the ratio
def ratio(a, b):
    return a / b

# List to store usernames
usernames = []

# Input usernames until the user stops
while True:
    insta_user = input("Enter your Instagram username (or type 'done' to finish): ")
    if insta_user.lower() == 'done':
        break
    usernames.append(insta_user)

# Process each username
for username in usernames:
    scrape(username)
