# Midjouney-Visual-Paraphase
This includes a script to invoke the bot and upload an image and then visually paraphrase these images based on the prompts in another file.esponding images, and download them

### Requirements:
- Python 3.10+
- `discord.py`, `selenium`, `pyautogui`, `requests` libraries

### Setup and Usage:

1. **Install Required Libraries**:
    ```bash
    pip install discord.py selenium pyautogui requests
    ```

2. **Run the Discord Bot**:
    ```bash
    python Discord.py
    ```

3. **Verify Bot Login**: Ensure the bot has logged into Discord.

4. **Configure and Run the Image Generation Script**:
    - Open `prompts_new.txt` and ensure it contains your prompts.
    - Update the prompt file name and image output folder paths in the script as needed.
    - Run the Midjourney.ipynb script.

### Notes:
- Use can check if the bot in Discord is working with the command:
  ```
  !upload_image <image_name>
  ```

### License:
- This project is licensed under the MIT License.
