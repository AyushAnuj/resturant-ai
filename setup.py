from setuptools import setup, find_packages

setup(
    name="restaurant-ai",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
        "langchain-core",
        "langchain-community",
        "langchain-ollama",
    ],
    entry_points={
        "console_scripts": [
            "restaurant-ai=restaurant_ai.run:main",
        ],
    },
)