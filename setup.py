from setuptools import setup, find_packages

setup(
       name='KuttyChurn',
       version='0.1.0',
       description='A package for predicting customer churn in E-Commerce data.',
       author='Your Name',
       packages=find_packages(),
       install_requires=[
           'pandas',
           'scikit-learn',
           'numpy',
           'matplotlib',
           'seaborn',
       ],
   )