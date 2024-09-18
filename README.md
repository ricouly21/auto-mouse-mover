Run the following commands:
```
# Create virtual environment
pyenv install 3.10
pyenv local 3.10
pyenv exec pip install virtualenv
pyenv exec python -m virtualenv venv
source venv/bin/activate

# Install pyautogui
pip install pyautogui

# Run main script
python main.py
```
