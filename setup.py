from setuptools import setup

setup(
    name='cabu',
    version='0.0.2',
    description='cabu is a simple REST microservice to scrap content from anywhere.',
    url='http://github.com/thylong/cabu',
    author='Theotime Leveque',
    author_email='theotime.leveque@gmail.com',
    license='BSD',
    platforms=['any'],
    packages=['cabu'],
    install_requires=[
        'requests',
        'beautifulsoup4>=2.9.1',
        'selenium>=2.50.0,<2.52.0',
        'xvfbwrapper>=0.2.7,<0.2.8',
        'flask>=0.10.1,<0.11.0',
        'six>=0.1.8',
        'requests-aws<1.11.0',
        'ftpretty>=0.2.3,<0.3.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=True
)
