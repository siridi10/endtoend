from setuptools import setup,find_packages
from typing import List

# declaring variable for setup function
Project_name="Housing-Predictior"
Version="0.0.2"
Author="Siridi Nath"
Desciption="Fist End to end project"
Requirement_file_name="requirements.txt"

def get_requirements_list()->List[str]:
    """
    desc:this function is going to return list of requirements mention in requirements.txt
    return:this function is going to return list of libraries mentioned in requirements.txt
    """
    
    with open(Requirement_file_name) as Requirement_file:
        return Requirement_file.readlines().remove("-e .")
setup(
name=Project_name,
version=Version,
author=Author,
package=find_packages(),
install_requires=get_requirements_list()
)