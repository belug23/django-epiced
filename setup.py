import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-epiced',
    version='0.4.3',
    packages=['epiced'],
    include_package_data=True,
    license='BSD License',
    description='A Django app to add the EpicEditor with easy to use widget.',
    long_description=README,
    url='https://github.com/belug23/django-epiced',
    install_requires=[
        'markdown',
    ],
    author='Belug',
    author_email='belug@oss.cx',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Text Editors',
    ],
)
