from setuptools import setup, find_packages


setup(
    name="bot_v2",
    version="0.1",
    description="Bot assistant",
    author="Prolisok team",
    author_email="alex.iesypenko@gmail.com",
    # Указываем, что пакеты находятся в src/
    packages=find_packages(where="src"),
    package_dir={"": "src"},              # Корневая директория пакета — src
    install_requires=[
        # Зависимости проекта
    ],
    entry_points={
        "console_scripts": [
            # Позволяет запускать `my_project` как команду
            "bot_v2=bot_v2.main:main",
        ],
    },
)
