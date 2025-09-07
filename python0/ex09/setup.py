from setuptools import find_packages, setup
# import re


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# def get_version():
#     with open("ft_package/__init__.py", "r", encoding="utf-8") as f:
#         content = f.read()
#     return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", content).group(1)


setup(
    # name="ft_package",
    # version=get_version(),
    # version="0.0.1",
    # description="A small package to learn how to pack",
    # package_dir={"": "ft_package"},
    packages=find_packages(),
    # entry_points={
    #     "console_scripts": [
    #         "ft_package = ft_package.count_in_list.__main__:main",
    #     ]
    # },
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url=": https://github.com/eseferi/ft_package",
    # need this url format since toml will give a format different from this
    # author="eseferi",
    # author_email="eseferi@42.fr",
    # license="MIT",
    # license_files=["LICENSE"],
    # classifiers=[
    #     "License :: OSI Approved :: MIT License",
    #     "Programming Language :: Python :: 3.10",
    #     "Operating System :: OS Independent",
    # ],
    # install_requires=["ipython >= 8.37.0"],
    # extras_require={
    #     "dev": ["pytest>=7.0", "twine>=4.0.2"],
    # },
    # python_requires=">=3.10",
)
