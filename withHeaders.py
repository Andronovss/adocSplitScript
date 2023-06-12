import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def split_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()

    current_header = ''
    current_content = ''
    header_found = False

    for line in content:
        if line.startswith('='):
            header_level = line.count('=')
            header = line.strip('= \n')
            if header_found:
                # Save the previous content to a file
                save_file(current_header, current_content)
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
        save_file(current_header, current_content)

def save_file(header, content):
    # Remove invalid characters from the header
    header = ''.join(c for c in header if c.isalnum() or c.isspace())
    
    # Create a directory for the file
    directory = os.path.join('output', header)
    create_directory(directory)
    
    # Save the content to a file with ".adoc" extension
    filename = os.path.join(directory, header + '.adoc')
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f'{content}')

# Замените 'input.adoc' на путь к вашему исходному файлу
split_file('input.adoc')
