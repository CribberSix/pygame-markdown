import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='pygame-markdown',
    packages=['pygamemarkdown'],
    include_package_data=True,
    license='MIT',
    description='A renderer for markdown text onto pygame surfaces.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/CribberSix/pygame-markdown',
    version='0.9.40',
    python_requires=">=3.6",
    author='CribberSix',
    author_email='cribbersix@gmail.com',
    install_requires=['pygame==1.9.6'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        #'Development Status :: 5 - Production/Stable',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development',
    ],
    keywords=['pygame', 'markdown', 'text', 'rendering'],
)

