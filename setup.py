from setuptools import setup


setup(
    name='django-parler-graphql',
    version='1.0.0',
    description='Django-parler-graphql is an app that allows querying of django-parler\'s translatable fields with '
                'Django GraphQL (graphene).',
    url='https://github.com/selmanceker/django-parler-graphql',
    maintainer='Selman Ceker',
    maintainer_email='selmanceker@gmail.com',
    install_requires=[
        'setuptools',
        'Django>=2.0',
        'django-parler>=1.9',
        'graphene>=2.1',
        'django-graphene>=2.1.0',
        'graphene-django-optimizer>=0.4.0',
    ],
    python_requires='>=3.5',
    platforms=['Any'],
    keywords=[
        'django', 'django-parler-graphql', 'django-parler', 'django-graphql', 'graphql', 'graphene', 'django-graphene',
        'python-graphene', 'python-graphql',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Django',
    ],
)
