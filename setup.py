from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .' # Used in requirements.txt 

def get_requirements(file_path:str) -> List[str]:
    '''
    The kind of input parameter given is like a path and it should read it 
    
    So, this function will return the list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # By default it will read lines from file_obj and will add \n in list while reading it
        # To removeit we will use following
        requirements = [req.replace("\n", "") for req in requirements]
        # After this we will add -e . in requirements to automatically trigger setup.py file

        # Now while running this code -e . will also come in requirements
        # To remove it we will use following
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements



# Below setup is writing of metadata information about the entire project 
setup(
    name='IndianHousePrice', 
    version= '0.0.1', 
    author= 'Swapnil', 
    author_email='sjikar65@gmail.com', 
    packages = find_packages(), 
    install_requires = get_requirements('requirements.txt')
)