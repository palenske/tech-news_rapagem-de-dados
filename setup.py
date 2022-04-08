from setuptools import setup

setup(
    name="tech_news",
    description="data scraping",
    install_requires=[
        "parsel==1.6.0",
        "requests==2.24.0",
        "pymongo==3.11.0",
        "dnspython==2.2.1"
        "python-decouple==3.3"
        "cssselect==1.1.0",
        "Flask==2.1.1",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "tech-news-collector=tech_news.menu:collector_menu",
            "tech-news-analyzer=tech_news.menu:analyzer_menu",
        ],
    },
)
