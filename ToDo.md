# Items to add to the project

[ ] Add message.py

[ ] Add password.py

[ ] Add DBlogin.py

[ ] Add spellNumber.py

[ ] Add include: with .py name & snippet to YAML

For better security at runtime, we break passwords into 2 parts. The first part creates the password and encryption key. The second part Gets the password and the encryption key.

- Create password:
  - Allows the user to create a password
  - The system always creates the key for encyrpting the password.
    - This way, keys are never transmitted and are always created and stored on the end-user's system
  - Whenever the user needs the password, we don't recreate, we Get Password. We only recreate if the uer wants a new password

- Create API:
  - Works the same was as a password. The user goes to the create API routine which then creates the key that will be used later when the user wants to GET API.


