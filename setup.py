from setuptools import find_packages, setup



setup(
    name='mlproject',
    version='0.0.1',
    author='Carlos de Olaguibel',
    author_email='carlos.de.olaguibel@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'tqdm',
        'requests',
        'joblib',
        'pytest',
        'pytest-cov'
    ]
)