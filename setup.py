from setuptools import setup, find_packages

try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = 'YGF Client using g4f.'

try:
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        install_requires = f.read().splitlines()
except FileNotFoundError:
    install_requires = ['g4f']

setup(
    name='ygf-client',
    version='0.1.0',
    description='Yandex GPT Free (YGF) client using g4f as backend and GPT-4 for imitation.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='MrN3lson',
    author_email='MrN3lson@getcontact.com',
    url='https://github.com/MrN3lson-Script/YGF-client',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
    ],
    python_requires='>=3.8',
)
