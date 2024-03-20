# Spelling Bee Inspired Puzzle Solver

This project is a web application inspired by the New York Times Spelling Bee puzzle. It allows users to input a set of letters, including a specific "center" letter, and find all possible words that meet the NYT Spelling Bee criteria: words must be at least 4 letters long, use letters from the input set only, and must include the center letter in each word.

## Features

- **Word Generation**: Generate all possible valid words based on input letters, adhering to specific puzzle conditions.
- **Web Interface**: A simple and intuitive web interface for inputting letters and displaying possible words.
- **Current Limitation**: The application currently supports generating words up to 10 letters long. Future optimizations are planned to accommodate longer words.

## Setup

### Requirements

- Python 3.6 or higher
- Flask
- An English words dictionary (see `english_words.get_english_words_set` usage)

### Installation

1. Clone this repository to your local machine.
2. Install required Python packages from the provided `requirements.txt` file:

   ```bash
   pip install -r requirements.txt


## Running the Application

Navigate to the project directory and run the Flask application:

```bash
python app.py

```
This will start a web server on `localhost:5000`. Open a web browser and go to `http://localhost:5000` to use the application.

## Usage

- On the web interface, input 6 letters in the provided fields and a center letter that must appear in all words.
- Click the submit button to view the results. The application will display all possible words that meet the criteria.

## Development Notes

Please note that this project is inspired by the NYT Spelling Bee puzzle but is not affiliated with the New York Times Company.

