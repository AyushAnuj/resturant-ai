from setuptools import setup, find_packages

setup(
    name="resturant-ai",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.30.0",
        "langchain-core",
        "langchain-community",
        "langchain-ollama",
    ],
    entry_points={
        "console_scripts": [
            "resturant-ai=resturant_ai.run:main",
        ],
    },
)