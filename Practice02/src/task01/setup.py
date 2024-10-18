from setuptools import setup

package_name = 'task01'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/task01.launch.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='grisha',
    maintainer_email='bimbam@example.com',
    description='Task 01: Receiver node for ROS2',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'receiver = task01.receiver:main',
	    'sender = task01.sender:main'
        ],
    },
)

