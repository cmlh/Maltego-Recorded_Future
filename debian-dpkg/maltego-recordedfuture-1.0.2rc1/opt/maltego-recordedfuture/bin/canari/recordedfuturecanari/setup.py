from setuptools import setup, find_packages

setup(
    name='recordedfuturecanari',
    author='Christian Heinrich',
    version='1.0',
    author_email='christian.heinrich@cmlh.id.au',
    description='https://github.com/cmlh/Maltego-Recorded_Future/',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari<=1.0'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
