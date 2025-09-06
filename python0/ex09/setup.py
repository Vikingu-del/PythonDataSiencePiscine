from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="ft_package",
    version="0.0.10",
    description="A small package to learn how to pack",
    # package_dir={"": "ft_package"},
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ft_package = ft_package.count_in_list.__main__:main",
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/etc",
    author="ft_segfault",
    author_email="rk.seferi@gmail.com",
    license="MIT",
    classifiers=[
        # "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["ipython >= 8.37.0"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
