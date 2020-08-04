import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anova-2ndgen-api", # Replace with your own username
    version="0.0.1",
    author="Billy Stevenson",
    author_email="anova-api@billystevenson.co.uk",
    description="A port of bmedicke's anova api for 2nd generation anova precision cookers (WiFi).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/Sotolotl/anova-2ndgen-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)