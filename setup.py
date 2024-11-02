from setuptools import setup, find_packages

setup(
    name="value_investing_app",
    packages=find_packages(),
    version="0.1",
    install_requires=[
        "streamlit",
        "plotly",
        "pandas",
        "requests",
        "python-dotenv",
    ],
) 