from setuptools import setup

setup(
    name="webface",
    version="0.1.0",
    install_required=[opencv-python],
    scripts=["bin/webface"]
)