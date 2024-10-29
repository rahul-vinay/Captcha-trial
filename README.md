# Captcha Trial

A simple Flask application that demonstrates CAPTCHA verification using Flask, Flask-Session, and Flask-Session-Captcha. This project integrates MongoDB for session management.

## Project Structure



## Features

- **CAPTCHA Verification**: Ensures that users are human before submitting forms.
- **MongoDB Integration**: Manages session data in MongoDB for persistent storage.
- **Flask-Session**: Utilizes server-side sessions to securely store session data.

## Requirements

- Python 3.11
- Flask
- Flask-Session
- Flask-Session-Captcha
- pymongo (for MongoDB)
- MongoDB (running on localhost)

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/captcha_trial.git
   cd captcha_trial

2. **Install Dependencies**
   ```bash
   pip install -U Flask Flask-Session Flask-Session-Captcha pymongo

3. **Run MongoDB (if it isn't running already)
   - Ensure MongoDB is installed and running on localhost:27017

4. **Run the Application**
   ```bash
   python app.py

5. **Access the Application**
   - Open your browser and go to http://localhost:5000
  
6. **Usage**
   - Visit the form at the route (/).
   - Fill in the CAPTCHA to verify that you are human.
   - Submit the form to see success or failure message.
