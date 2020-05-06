from setuptools import setup

setup(
    name='yaz-it',
    version='0.3.0',
    author='NiceneNerd',
    author_email='macadamiadaze@gmail.com',
    description='Quick tool for yaz0 compression/decompression',
    url='https://github.com/NiceneNerd/yaz-it',
    packages=['yazit'],
    entry_points = {
        'console_scripts': [
            'yazit = yazit.yazit:main',
            'yaz = yazit.yazit:main',
            'unyazit = yazit.unyazit:main',
            'unyaz = yazit.unyazit:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only'
    ],
    python_requires='>=3.7',
    install_requires=[
        'oead>=1.0.0',
    ]
)
