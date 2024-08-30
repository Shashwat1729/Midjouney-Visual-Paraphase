# Midjourney Visual Paraphrase

This project provides a Python script to invoke a Discord bot that uploads images and generates visual paraphrases based on provided prompts. It leverages Midjourney's image generation capabilities to create unique visual interpretations.

## Features

- **Automated Image Upload**: The bot uploads images to Discord.
- **Visual Paraphrasing**: Generates new images based on user-defined prompts.
- **Customizable**: Adjust prompts and output paths for personalized results.

## Requirements

- Python 3.10+
- Libraries: `discord.py`, `selenium`, `pyautogui`, `requests`

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Shashwat1729/Midjouney-Visual-Paraphase.git
    cd Midjouney-Visual-Paraphase
    ```
2. Install the required Python libraries:
    ```bash
    pip install discord.py selenium pyautogui requests
    ```

## Usage

1. **Run the Discord Bot**:
    ```bash
    python Discord.py
    ```
   Ensure the bot logs in to Discord.

2. **Configure and Execute**:
   - Edit `prompts_new.txt` with your custom prompts.
   - Adjust file paths in the script as necessary.
   - Execute the image generation script:
     ```bash
     jupyter notebook Midjourney_para.ipynb
     ```

3. **Upload and Paraphrase**:
   - Use the bot command in Discord to upload an image:
     ```bash
     !upload_image <image_name>
     ```
   - The bot will generate and download the paraphrased images.

## Notes

- Adjust the sleep time in the script if you encounter issues with bot speed.
- Ensure the prompt file and image output directories are correctly configured.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

