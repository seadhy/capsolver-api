from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()


classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

setup(
    name='capsolver_api',
    version='1.0.5',
    author='seadhy',
    author_email='seadhy@protonmail.com',
    description='capsolver.com library for Python',
    long_description=long_description,
    license="MIT",
    long_description_content_type='text/markdown',
    url='https://github.com/seadhy/capsolver-api',
    project_urls={
        'Documentation': 'https://github.com/seadhy/capsolver-api#capsolver-api-for-python',
        'Source': 'https://github.com/seadhy/capsolver-api/tree/main/capsolver_api',
        'Bug Tracker': 'https://github.com/seadhy/capsolver-api/issues',
    },
    classifiers=classifiers,
    install_requires=['requests'],
    packages=['capsolver_api', 'capsolver_api.tasks', 'capsolver_api.recognitions'],
    include_package_data=True,
    python_requires='>=3',

)
