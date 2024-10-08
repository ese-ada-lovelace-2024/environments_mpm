from setuptools import setup, find_packages

setup(
    name='envtest',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="Playing with virtual environments.",
    long_description="Playing with virtual environments.",
    author="Imperial College London",
    author_email='rhodri.nelson@imperial.ac.uk',
    packages=find_packages(),
==================
    version='0.1.0',  # You can use any version you prefer
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your package dependencies here
    ],

)
