import setuptools


with open('README.md', 'r', encoding="utf-8") as rf:
    long_description = rf.read()

setuptools.setup(
    name='simple-serializer-NIKITA-KOZNEV',
    version='1.0.2',
    author='Nikita Koznev',
    author_email='nikitakoznev@gmail.com',
    description='Python Simple Serializer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/spanickroon/Python-Simple-Serializers',
    project_urls={
        'Bug Tracker': 'https://github.com/spanickroon/Python-Simple-Serializers/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=['formatserializer', 'formatserializer.tests', 'formatserializer.testing'],
    python_requires=">=3.8",
    install_requires=[
        'PyYAML==5.4.1',
        'toml==0.10.0'
    ],
)
