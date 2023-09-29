import setuptools

README = ''
PACKAGE_LIST = []
with open('README.md','r') as f:
    README = f.read()
with open('package_list.txt','r') as f:
    PACKAGE_LIST = eval(f.read())

setuptools.setup(
    name = "spring",
    version = "1.0",
    author = "ArksTeam | Jankie",
    author_email = "Jankie@edu.awaish.link",
    description = "",
    long_description = README,
    zip_safe = False,
    packages = PACKAGE_LIST,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent"
    ]
)