from setuptools import setup

setup(
    name="tech_news",
    description="data scraping",
    install_requires=[
        "parsel==1.6.0",
        "requests==2.24.0",
        "pymongo==4.1.0",
        "dnspython==2.2.1"
        "python-decouple==3.3"
        "cssselect==1.1.0",
        "Flask==2.1.1",
    ],
)
