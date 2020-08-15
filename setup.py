import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynamic-motion-planner", 
    version="0.0.1",
    author="Lance",
    author_email="lancemok92@gmail.com",
    description=" ... python robotics path planner package with ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lancemk/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
