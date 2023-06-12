import os
import argparse

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def split_file(filename, file_format):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()

    current_header = ''
    current_content = ''
    header_found = False

    for line in content:
        if line.startswith('=') or line.startswith('#'):
            header_level = line.count('=') + line.count('#')
            header = line.strip('=# \n')
            if header_found:
                # Save the previous content to a file
                save_file(current_header, current_content, file_format)
            current_header = header
            current_content = ''
            header_found = True
            # Create nested directories based on header level
            directory_parts = header.split()[0:]
            if len(directory_parts) > 1:
                directory = os.path.join('output', ' '.join(directory_parts))
            else:
                directory = os.path.join('output', *directory_parts)
            create_directory(directory)
        current_content += line
    
    # Save the last section to a file
    if header_found:
        save_file(current_header, current_content, file_format)

def save_file(header, content, file_format):
    # Remove invalid characters from the header
    header = ''.join(c for c in header if c.isalnum() or c.isspace())
    
    # Create a directory for the file
    directory = os.path.join('output', header)
    create_directory(directory)

    # Determine the file extension based on the file format
    if file_format == 'adoc':
        extension = '.adoc'
    elif file_format == 'md':
        extension = '.md'
    else:
        raise ValueError(f"Unsupported file format: {file_format}")
    
    # Save the content to a file with ".adoc" extension
    filename = os.path.join(directory, header + extension)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f'{content}')

# Creating a command-line argument parser
parser = argparse.ArgumentParser(description='Split a large AsciiDoc or Markdown files based on headers.')
parser.add_argument('filename', type=str, help='Path to the input file')
parser.add_argument('--format', type=str, choices=['adoc', 'md'], default='adoc', help='Output file format (adoc or md)')

# Getting command-line arguments
args = parser.parse_args()

# Call the split_file function, passing the file name and format
split_file(args.filename, args.format)