import setuptools

setuptools.setup(
    name="jupyter-prefect-proxy",
    version="1.0dev",
    url="https://github.com/danielhstahl/jupyter-prefect-proxy",
    author="Daniel Stahl",
    description="danstahl1138@gmail.com",
    packages=setuptools.find_packages(),
    keywords=["Jupyter"],
    classifiers=["Framework :: Jupyter"],
    install_requires=["jupyter-server-proxy", "prefect"],
    entry_points={
        "jupyter_serverproxy_servers": [
            "jupyter-prefect-proxy = jupyter_prefect_proxy:setup_prefect",
        ]
    },
    package_data={
        "jupyter_prefect_proxy": ["icons/*"],
    },
)
