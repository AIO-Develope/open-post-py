# client.py
import requests
import os
BASE_URL = 'http://127.0.0.1:5001'

def create_post(username, text):
    url = f'{BASE_URL}/post'
    data = {'username': username, 'text': text}
    response = requests.post(url, json=data)
    print(response.json()['message'])
    

def get_posts():
    url = f'{BASE_URL}/posts'
    response = requests.get(url)
    posts = response.json()['posts']
    print(f"{'-'*20}")
    if posts:
        for post in posts:
            print(f"Username: {post['username']}\nText: {post['text']}\n{'-'*20}")
    else:
        print("No posts available.")

if __name__ == '__main__':
    while True:
        print("\n1. Create Post\n2. Get Posts\n3. Exit")
        choice = input("Enter your choice: ")
        os.system("cls")
        if choice == '1':
            username = input("Enter your username: ")
            text = input("Enter your post text: ")
            create_post(username, text)
        elif choice == '2':
            get_posts()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
