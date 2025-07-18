# Module to compare two files for updates.

import os

def ist_aktualisiert():
    """
    Compares two files, Ziel.txt and Ziel_alt.txt, to see if Ziel.txt has been updated.

    This function is designed to be extensible for future enhancements,
    such as semantic comparison or version tracking.

    Returns:
        bool: True if Ziel.txt is different from Ziel_alt.txt, False otherwise.
    """
    # Define file paths
    # IMPORTANT: Rename 'Gedachtnis' to 'Gedächtnis' in your environment.
    file_new = os.path.join('Gedachtnis', 'Ziel.txt')
    file_old = os.path.join('Gedachtnis', 'Ziel_alt.txt')

    # Check for existence of both files
    if not os.path.exists(file_new) or not os.path.exists(file_old):
        print("Error: One or both files not found.")
        return False

    # Read the content of both files
    with open(file_new, 'r', encoding='utf-8') as f_new, open(file_old, 'r', encoding='utf-8') as f_old:
        content_new = f_new.read()
        content_old = f_old.read()

    # Compare the content
    if content_new != content_old:
        print("Ziel.txt has been updated.")
        # Future extension: Log the specific differences
        # For now, we just print a general message.
        print("Differences detected.")
        return True
    else:
        print("No changes detected in Ziel.txt.")
        return False

# Example usage (for testing purposes)
if __name__ == '__main__':
    # Create dummy files for testing
    if not os.path.exists('Gedachtnis'):
        os.makedirs('Gedachtnis')

    with open(os.path.join('Gedachtnis', 'Ziel.txt'), 'w', encoding='utf-8') as f:
        f.write("This is the new version.\n")
    with open(os.path.join('Gedachtnis', 'Ziel_alt.txt'), 'w', encoding='utf-8') as f:
        f.write("This is the old version.\n")

    ist_aktualisiert()

    print("-" * 20)

    with open(os.path.join('Gedachtnis', 'Ziel.txt'), 'w', encoding='utf-8') as f:
        f.write("This is the old version.\n")

    ist_aktualisiert()
