# Sanity_Tests For Outlook

## Overview
- This repo contains the code for the testing performed on Outlook.
- Prompt used for testing: What is Project Bluefin?

## Location of the test file:
- Outlook_testing -> tests -> test_sanity.py

## Tasks performed:
- Login using the .env file, which contains the username and password.
- Prompt used: What is Project Bluefin?
- Writing the prompt on the draft section under "New Email" in Outlook.
- Then click on the Copilot icon to "Auto-rewrite" for the prompt written in the draft section.
- Acushield throws a warning for this prompt and using locators, I was able to click on the **Proceed** option.

## Challenges faced:
No challenges we faced in this part, as the html elements were easy to interact with.
There were no shadow DOM or hidden iframes which posed a problem.
**Playwright Inspector** was very helpful in finding the locators and CSS selectors for interaction.
