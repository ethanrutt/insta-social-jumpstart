# insta-social-jumpstart
Automated bot for sending recruiting messages using selenium in python


Hello, this is my first github repository that i've created by myself. It is just a simple script for sending messages on instagram.
It uses selenium to open up an instance of a chrome tab, login to an instagram, and copy paste a message to people. 

- The username and password fields in the class must be set to the desired login
- The message must be initialized to a string so that the bot knows what to send

I used this to send recruiting messages to leads that I collected while I was working as a branch manager for vector marketing in the summer 0f 2022

IMPORTANT NOTE: Selenium uses the XPATH to find the elements to click on, however instagram changes their html often so the XPATH could change, and this will cause bugs as it will not be able to find the elements to click on. I don't plan to update this so if the XPATH's are changed, then this program will not work anymore.
