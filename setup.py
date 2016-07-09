"""Setup."""
from distutils.core import setup


setup(
    name='timr.ebook.core',
    version='0.1',
    description='E-book sentence generation utils',
    author='Robert Wallhead',
    author_email='robert@thisismyrobot.com',
    url='http://thisismyrobot.com/',
    packages=[
        'timr',
        'timr.ebook',
    ],
)
