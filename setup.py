from setuptools import find_packages, setup

url = ""
version = "0.1.0"
readme = open("README.md").read()

setup(
    name="icon-network-exporter",
    packages=["icon_network_exporter"],
    version=version,
    description="exporter agent for icon blockchain",
    long_description=readme,
    entry_points={
        "console_scripts": [
            "icon-network-exporter=icon_network_exporter:main",
        ],
    },
    install_requires=[
        "requests>=2,<3",
        "prometheus_client",
        "pydantic",
        "aiohttp",
        "PyYAML",
        "async-timeout",
    ],
    include_package_data=True,
    author="Rob Cannon",
    author_email="rob.cannon@insightdatascience.com",
    url=url,
    download_url="{}/tarball/{}".format(url, version),
    license="MIT",
)
