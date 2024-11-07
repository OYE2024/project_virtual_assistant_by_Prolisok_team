from setuptools import setup, find_packages


setup(
    name="BOT_V2_main",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "BOT_V2_main=BOT_V2.main:main",
        ],
    },
)
