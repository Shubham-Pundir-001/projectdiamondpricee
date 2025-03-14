from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."

def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements





setup(
      name="DiamondPricePrediction",
      version='0.0.1',
      author="shubham",
      author_email="shubhamrnamac@gmail.com",
      install_require=get_requirement('requirement.txt'),
      package=find_packages()

)