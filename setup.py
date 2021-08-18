import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='pyodbc-lambda-python3.8',  
     version='0.1',
     scripts=['pyodbc-lambda-python3.8'] ,
     author="Radoslaw Wielonski",
     author_email="radoslaw.wielonski@nordcloud.com",
     description="Pre-built package of pyodbc and ODBC 17 SQL Server driver",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/radoslaw-wielonski-nc/pyodbc-lambda-python3.8",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.8",
         "License :: OSI Approved :: MIT License",
         "Operating System :: Amazon Linux",
     ],
 )