from setuptools import setup

setup(
    name='drumline',
    version='0.0.1',
    packages=['drumline'],
    url='https://github.com/HP824/drumline',
    license='Unlicense',
    author='Harish Prabhakaran',
    author_email='harish@prabha.me',
    description='Code to create custom drumline objects',
    setup_requires=['flake8'],
    entry_points={
        'console_scripts': [
            'drumline = drumline.app.main:main'
        ]
    }
)