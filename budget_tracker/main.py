from budget_tracker.files_manager import create_file
from budget_tracker.user_input import user_input

def main():
    create_file()
    user_input()


if __name__ == "__main__":
    main()

"""
The pragmatic test-user flow right now:

They clone the repo
python3 -m venv venv && source venv/bin/activate
pip install -e .
Done
"""