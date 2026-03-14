from budget_tracker.files_manager import create_file

def main():
    print(f"File path: {create_file()}")
    create_file()


if __name__ == "__main__":
    main()