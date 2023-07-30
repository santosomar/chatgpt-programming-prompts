import os

# Table of Contents
table_of_contents = {
    "Introduction": "Learning computer programming can be an exciting and rewarding experience.",
    "Getting Started": "If you are new to programming, this section is the best place to begin.",
    "Programming Languages": "This section covers multiple programming languages to give you a diverse learning experience.",
    "Topics Covered": "This section covers a wide range of programming topics to help you grow as a programmer.",
    "Contributing": "We welcome contributions from the community to make this repository even more helpful to aspiring programmers.",
    "License": "This repository is licensed under the MIT License."
}

# Function to create directories and README.md files
def create_directories_with_readme():
    for section, content in table_of_contents.items():
        # Create a directory for each section
        os.makedirs(section, exist_ok=True)
        
        # Create the README.md file inside the directory
        readme_file_path = os.path.join(section, "README.md")
        with open(readme_file_path, "w") as readme_file:
            readme_file.write(f"# {section}\n\n{content}\n")

if __name__ == "__main__":
    create_directories_with_readme()
    print("Directories and README.md files created successfully!")
