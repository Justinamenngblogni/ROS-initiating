from setuptools import find_packages, setup

package_name = 'my_package_python_justin'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Justin',
    maintainer_email='justin.ngblogni@etu.unilim.fr',
    description='Beginner client libraries tutorials practice package. Done at Turin',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_node = my_package_python_justin.my_node:main'
        ],
    },
)
