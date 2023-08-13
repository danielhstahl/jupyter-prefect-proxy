import setuptools

setuptools.setup(
    name="jupyter-prefect-proxy",
    version="1.2dev",
    url="https://github.com/danielhstahl/jupyter-prefect-proxy",
    author="Daniel Stahl",
    description="danstahl1138@gmail.com",
    packages=setuptools.find_packages(),
    keywords=["Jupyter", "Prefect"],
    classifiers=["Framework :: Jupyter"],
    install_requires=["jupyter-server-proxy"],
    entry_points={
        "jupyter_serverproxy_servers": [
            "prefect = jupyter_prefect_proxy:setup_prefect",
        ]
    },
    package_data={
        "jupyter_prefect_proxy": ["icons/*"],
    },
)
