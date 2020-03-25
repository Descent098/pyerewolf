import setuptools

def get_content(*filename):
    """ Gets the content of a file and returns it as a string
    Args:
        filename(str): Name of file to pull content from
    Returns:
        str: Content from file
    """
    content = ""
    for file in filename:
        with open(file, "r") as full_description:
            content += full_description.read()
    return content

setuptools.setup(
    name = "pyerewolf",
    version = "0.0.1",
    author = "Kieran Wood",
    author_email = "kieran@canadiancoding.ca",
    description = "A web version of the werewolf game implemented in python using Flask.",
    long_description = get_content("README.md", "CHANGELOG.md"),
    long_description_content_type = "text/markdown",
    project_urls = {
        "User Docs" :  "https://kieranwood.ca/pyerewolf",
        "Source" :     "https://github.com/Descent098/pyerewolf",
    },
    include_package_data = True,
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning"
    ],
)