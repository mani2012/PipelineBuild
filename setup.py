from setuptools import setup, find_packages

setup(
    name="PipelineBuild",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pipelinebuild = pipelinebuild.__main__:main"
        ]
    },
    namespace_packages=["pipelinebuild"]
    )
