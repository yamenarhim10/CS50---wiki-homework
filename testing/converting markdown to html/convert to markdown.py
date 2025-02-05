import markdown2
import os

def convert_markdown_to_txt(markdown_file):
    # Check if the file exists
    if not os.path.exists(markdown_file):
        print(f"The file {markdown_file} does not exist.")
        return

    # Read the Markdown file
    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    # Convert Markdown to HTML
    html = markdown2.markdown(markdown_text)

    # Define the output text file name
    base_name = os.path.splitext(markdown_file)[0]
    txt_file = f"{base_name}.txt"

    # Write the HTML content to the text file
    with open(txt_file, 'w', encoding='utf-8') as file:
        file.write(html)

    print(f"Converted {markdown_file} to {txt_file}")

if __name__ == "__main__":
    # Replace 'example.md' with your Markdown file name
    markdown_file = 'Django.md'
    convert_markdown_to_txt(markdown_file)