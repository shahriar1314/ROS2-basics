from setuptools import setup

package_name = 'pulse_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Package with GUI to control Boolean pulse publisher',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pulse_node = pulse_control.pulse_node:main',
            'pulse_ui = pulse_control.pulse_ui:main',
        ],
    },
)
