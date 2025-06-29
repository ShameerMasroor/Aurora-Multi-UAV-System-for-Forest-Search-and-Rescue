from setuptools import setup
from glob import glob
import os

package_name = 'sjtu_drone_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, "launch"), glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name, "rviz"), glob('rviz/*.rviz')),
        (os.path.join('share', package_name, "config"), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='georg.novtony@aon.at',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawn_drone = sjtu_drone_bringup.spawn_drone:main',
            'pose_to_path_node = sjtu_drone_bringup.gt_path:main',  # Added PoseToPathNode entry
            'segmentation_node = sjtu_drone_bringup.segmentation:main',
            'mission_end_node = sjtu_drone_bringup.mission_end:main',
            'yaw_diff_node = sjtu_drone_bringup.yaw_diff_storer:main',
        ],
    },
)