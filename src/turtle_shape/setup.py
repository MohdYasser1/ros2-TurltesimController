from setuptools import find_packages, setup

package_name = 'turtle_shape'

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
    maintainer='mohd_yasser1',
    maintainer_email='mohd_yasser100@gmail.com',
    description='This pakage draws shape in turtlesim',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'shapeNode = turtle_shape.shapeNode:main',
            'turtleCommander = turtle_shape.turtleCommander:main'
        ],
    },
)
