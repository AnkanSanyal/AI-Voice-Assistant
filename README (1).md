
# AI Voice Assistant - Jarvis

Jarvis is an AI voice assistant built using Python that can perform a variety of tasks such as opening websites, fetching information from Wikipedia, sending emails, telling jokes, and more. It uses a range of Python libraries to process voice commands and perform tasks.


## Table of Contents

1.Features

2.Prerequisites

3.Installation

4.Usage

5.Tech Stack

6.Contributing

7.License
## Features

- Convert speech to text and respond with voice.
- Fetch information from Wikipedia.
- Open websites and applications.
- Send emails through SMTP.
- Tell jokes and manage system tasks.
- Control system volume, battery status, and more.


## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.6 or higher
- Pycharm
- Required Python libraries (listed below)
## Installation

1.Clone the repository:

```bash
  git clone https://github.com/AnkanSanyal/AI-Voice-Assistant.git
  cd AI-Voice-Assistant

```

2.Install the required Python libraries:

```bash
  pip install pyttsx3 speechrecognition datetime wikipedia smtplib webbrowser os pyautogui psutil pyjokes


```

3.Set up email configuration (optional):
- If you want to use the email functionality, update the email credentials in the script (use environment variables or configuration files for security).
## Used By
1.Run the Script:
```bash
  python jarvis.py
```
2.Example Commands:

- "What’s the weather today?"
- "Send an email to [contact name]."
- "Tell me a joke."
- "What's the time?"
- "Search Wikipedia for Python programming."



## Tech Stack

- **Speech-to-Text**: speech_recognition
- **Text-to-Speech**: pyttsx3
- **Email**: smtplib
- **Web Browsing**: webbrowser
- **System Automation**: os, pyautogui, psutil
- **Information Fetching**: wikipedia
- **Entertainment**: pyjokes


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.Fork the repository.

2.Create a new branch (git checkout -b feature-branch).

3.Make your changes.

4.Commit your changes (git commit -m 'Add some feature').

5.Push to the branch (git push origin feature-branch).

6.Open a pull request.


## License

This project is licensed under the MIT License - see the [license](https://choosealicense.com/licenses/mit/) file for details.

