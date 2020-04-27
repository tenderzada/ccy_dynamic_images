import setuptools
from distutils.core import setup
setup(
    name='ccy_dynamic_image',
    version='0.1',
    description='add dynamic effect to text or image',
    author='Chen Jiao',
    author_email='chenjiao@mail.ynu.edu.com',
    url='https://github.com/pythonml/douyin',
    packages=setuptools.find_packages(),
    install_requires=['Pillow>=7.0.0', 'numpy==1.16.2'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'ccy_dynamic_image=ccy_dynamic_image:main'
        ],
    },
)
