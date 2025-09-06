Required for this to work during studying with setup.py and wheel and etc
    python setup.py bdist_wheel
    pip install wheel
    pip install --upgrade build
    pip install --upgrade setuptools[core]
    creating 

.
├── LICENSE
├── README.md
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       └── count_in_list
│           └── __init__.py
├── dist
│   ├── ft_package-0.0.10-py3-none-any.whl
│   └── ft_package-0.0.10.tar.gz
├── ft_package
│   ├── __init__.py
│   ├── count_in_list
│   │   ├── __init__.py
│   │   ├── src
│   │   │   └── count_in_list.py
│   │   └── test
│   └── ft_package.egg-info
│       ├── PKG-INFO
│       ├── SOURCES.txt
│       ├── dependency_links.txt
│       ├── requires.txt
│       └── top_level.txt
├── pyproject.toml
├── run.py
└── setup.py

2 ways to build
    1. using setuptools with setup.py
        inside setup.py we can import
            from setuptools import find_packages, setup
        function setup is the entry point where you declare metadata and build configuration when you’re still using the legacy setup.py system
        Is getting deprecated
        this are all the attributes that the function can take:
            (function) def setup(
                *,
                name: str = ...,
                version: str = ...,
                description: str = ...,
                long_description: str = ...,
                author: str = ...,
                author_email: str = ...,
                maintainer: str = ...,
                maintainer_email: str = ...,
                url: str = ...,
                download_url: str = ...,
                packages: list[str] = ...,
                py_modules: list[str] = ...,
                scripts: list[str] = ...,
                ext_modules: list[Extension] = ...,
                classifiers: list[str] = ...,
                distclass: type[Distribution] = ...,
                script_name: str = ...,
                script_args: list[str] = ...,
                options: Mapping[str, Incomplete] = ...,
                license: str = ...,
                keywords: list[str] | str = ...,
                platforms: list[str] | str = ...,
                cmdclass: Mapping[str, type[Command]] = ...,
                data_files: list[tuple[str, list[str]]] = ...,
                package_dir: Mapping[str, str] = ...,
                obsoletes: list[str] = ...,
                provides: list[str] = ...,
                requires: list[str] = ...,
                command_packages: list[str] = ...,
                command_options: Mapping[str, Mapping[str, tuple[Incomplete, Incomplete]]] = ...,
                package_data: Mapping[str, list[str]] = ...,
                include_package_data: bool | Literal[0, 1] = ...,
                libraries: list[str] = ...,
                headers: list[str] = ...,
                ext_package: str = ...,
                include_dirs: list[str] = ...,
                password: str = ...,
                fullname: str = ...,
                **attrs: Any
            ) -> Distribution


To be able to create your package:
    1. First we have to choose our build backend.
        In our case setuptools
    2. Since we are using setuptools we have to create
    a pyproject.toml file and specify the requirements and the build-backend
        