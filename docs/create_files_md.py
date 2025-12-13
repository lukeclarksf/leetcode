import os

def create_md_files(start_num, end_num, content=None):
    if start_num > end_num:
        print("Error: The starting number must be less than or equal to the ending number.")
        return

    if content is None:
        default_content = ""

    print(f"Starting to create files from {start_num}.md to {end_num}.md...")
    
    for i in range(start_num, end_num + 1):
        filename = f"{i}.md"
        content = '```pyodide\n\
{% \n\
    include "../python/'+f"{i}"+'.py" \n\
    preserve-includer-indent=false \n\
%}\n\
```\n\
\n\
```python\n\
{% \n\
    include "../python/'+f"{i}"+'.py" \n\
    preserve-includer-indent=false \n\
%}\n\
```'
        file_content = content if content is not None else default_content + str(i)

        try:
            with open(filename, 'w') as f:
                f.write(file_content + "\n")

        except IOError as e:
            print(f"An error occurred while creating {filename}: {e}")
            
    print("File creation complete!")

START_NUMBER = 19
END_NUMBER = 320
FILE_CONTENT = None

create_md_files(START_NUMBER, END_NUMBER, FILE_CONTENT)