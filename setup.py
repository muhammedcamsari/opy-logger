import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opy-logger",
    version="1.0",
    author="Muhammed Çamsarı",
    license='MIT',
    author_email="Muhammedcamsari@icloud.com",
    description="Used for simple log output.",
    long_description=long_description,
    url="https://github.com/muhammedcamsari/opy-logger",
    long_description_content_type="text/markdown",
    keywords=['log', 'logger', 'simple'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    py_modules=['opylogger'],
    entry_points='''
        [console_scripts]
        opylogger=opylogger:opylogger
    ''',
)