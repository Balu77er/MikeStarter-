# Module to read the content of AntwortCopilot.txt.

import os

def get_antwort_content():
    """
    Reads the content of AntwortCopilot.txt from the Gedachtnis directory.

    Returns:
        str: The content of the file, or an error message if the file
             is missing, empty, or unreadable.
    """
    # IMPORTANT: Rename 'Gedachtnis' to 'Gedächtnis' in your environment.
    file_path = os.path.join('Gedachtnis', 'AntwortCopilot.txt')

    # Check if the file exists
    if not os.path.exists(file_path):
        return "Error: AntwortCopilot.txt not found."

    # Check if the file is not empty
    if os.path.getsize(file_path) == 0:
        return "Error: AntwortCopilot.txt is empty."

    try:
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading AntwortCopilot.txt: {e}"

# Example usage (for testing purposes)
if __name__ == '__main__':
    # Create a dummy file for testing
    if not os.path.exists('Gedachtnis'):
        os.makedirs('Gedachtnis')

    # Test case 1: File with content
    with open(os.path.join('Gedachtnis', 'AntwortCopilot.txt'), 'w', encoding='utf-8') as f:
        f.write("This is the response from the Copilot.")
    print(get_antwort_content())

    # Test case 2: Empty file
    with open(os.path.join('Gedachtnis', 'AntwortCopilot.txt'), 'w', encoding='utf-8') as f:
        pass
    print(get_antwort_content())

    # Test case 3: Missing file
    os.remove(os.path.join('Gedachtnis', 'AntwortCopilot.txt'))
    print(get_antwort_content())
