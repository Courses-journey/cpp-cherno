###############
### ChatGPT ###
###############
import os
import codecs


def to_snake_case(string):
    # replace all non-alphanumeric characters (except +) with underscores
    underscored = "".join(c if c.isalnum() or c ==
                          "+" else "_" for c in string)
    # convert to lowercase and split at underscores
    words = underscored.lower().split("_")
    # join words with underscores
    return "_".join(words)


# specify the directory where the README.md file is located
dir_path = os.getcwd()

# specify the course folder where the new files will be created
course_folder = "course"

# specify the repo url base
repo_url_base = "https://github.com/Courses-journey/cpp-cherno"

# check if the course folder exists, create it if it doesn't
if not os.path.exists(os.path.join(dir_path, course_folder)):
    os.makedirs(os.path.join(dir_path, course_folder))

# read the contents of the README.md file using UTF-8 encoding
with codecs.open(os.path.join(dir_path, "README.md"), "r", encoding="utf-8") as readme:
    # initialize the title, content, and counter variables
    title = None
    content = ""
    counter = 1
    links = []

    # loop through each line of the README.md file
    for line in readme:
        # check if the line is a first-level heading
        if line.startswith("# "):
            # if there is an existing title and content, create a new file with that title and content
            if title and content:
                output_name = f"{counter:03}-{to_snake_case(title)}"
                subdir_path = os.path.join(
                    dir_path, course_folder, output_name)
                if not os.path.exists(subdir_path):
                    os.makedirs(subdir_path)
                file_name = f"{output_name}.md"
                new_file_path = os.path.join(subdir_path, file_name)
                with open(new_file_path, "w", encoding="utf-8") as new_file:
                    new_file.write(f"# {title}\n\n{content}")
                # add link to the list of links
                link = title
                links.append(link)
                # increment the counter and reset the content variable
                counter += 1
                content = ""

            # update the title variable with the new title
            title = line.strip()[2:]
        # if the line is not a first-level heading, add it to the content variable
        else:
            content += line

    # create the last file with the final title and content
    output_name = f"{counter:03}-{to_snake_case(title)}"
    subdir_path = os.path.join(dir_path, course_folder, output_name)
    if not os.path.exists(subdir_path):
        os.makedirs(subdir_path)
    file_name = f"{output_name}.md"
    new_file_path = os.path.join(subdir_path, file_name)
    with open(new_file_path, "w", encoding="utf-8") as new_file:
        new_file.write(f"# {title}\n\n{content}")
    # add link to the list of links
    link = title
    links.append(link)

# create the course_content.md file with links to the course files
course_content_path = os.path.join(dir_path, "course_content.md")
with open(course_content_path, "w", encoding="utf-8") as course_content_file:
    course_content_file.write(f'''
# cpp-cherno

The Cherno youtube channel

* [c++ course](https://www.youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb)

''')

    content_count = 1
    for link in links:
        output_name = f"{content_count:03}-{to_snake_case(link)}"
        content_link = f"{repo_url_base}/{course_folder}/{output_name}/{output_name}.md"

        course_content_file.write(f"## {content_count:03} - {link}\n")
        course_content_file.write(f"* [Notes]({content_link})\n")

        content_count += 1
