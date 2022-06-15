from setuptools import setup, find_packages

setup(
    name='protect',
    version='0.1',
    python_requires='>=3.8',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pytest',
        'pytest-mypy',
        'pyyaml',
        'colorama',
        'gitignore_parser',
        'pid',
    ],
    entry_points='''
        [console_scripts]
        protect=src.cli:main
    ''',

    author="Preston Hunt",
    author_email="me@prestonhunt.com",
    description="Protect",
    keywords="chunk chunk-based backup asymmetric public-key lockss",
    url="https://github.com/presto8/protect",
)
