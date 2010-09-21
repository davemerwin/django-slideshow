from setuptools import setup, find_packages

setup(
    name='django-slideshow',
    version=__import__('slideshow').__version__,
    description='Django Slideshow is a simple slideshow app for adding slideshows to your projects.',
    long_description=open('README.rst').read(),
    author='Pure Blue Design',
    author_email='dave@purebluedesign.com',
    url='http://github.com/davemerwin/django-slideshow/tree',
    download_url='http://github.com/davemerwin/django-slideshow/archives/master',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

