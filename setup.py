from setuptools import setup, find_packages  
  
setup(  
    name = "EasyGitTool",  
    version = "1.4",  
    long_description = "EasyGitTool for python",  
    license = "Apache License", 
    url = "https://easygittool.github.io",  
    author = "Mryan2005",  
    author_email = "A2564011261@163.com",  
    packages = find_packages(),  
    include_package_data = True,  
    platforms = "any",  
    install_requires = [],  
    keywords=["EasyGitTool"],
    scripts = [],  
    entry_points = {  
        'console_scripts': [  
            'gt = EasyGitTool.main:main'  
        ]  
    }  
)
