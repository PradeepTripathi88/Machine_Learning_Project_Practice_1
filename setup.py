from setuptools import setup, find_packages
from typing import List

project_name = "myproject"
version ="0.0.1"
author = "Pradeep"
description = "this is my project testing "

req_file_name = "requirements.txt"
current_package = "-e ."

def get_requirements_txt() ->List[str]:
    with open(req_file_name,'r') as req:
        req_list = req.readlines()
        req_list = [i.replace("\n", "") for i in req_list]
        if current_package in req_list:
            req_list.remove(current_package)
        return req_list

setup(name=project_name,
      version=version,
      author=author,
      description=description,
      package=find_packages(),
      install_requrement=get_requirements_txt())

