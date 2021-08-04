try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyami_p',
    url='https://github.com/petermr/pyami',
    version='0.0.3',
    author="Peter Murray-Rust",
    include_package_data=True,
    license='Apache2',
    install_requires=[],
    author_email='petermurrayrust@googlemail.com',
    long_description=open('README.md').read(),
    zip_safe=False,
    keywords='text and data mining',
    packages=[
        'pyami_m',
        ],
    classifiers=[
        'Development Status :: 0.1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        "console_script" :
            ["py4ami=pyami_m.pyamix:main"]
    }
)

