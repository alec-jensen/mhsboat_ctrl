from setuptools import find_packages, setup

package_name = "mhsboat_ctrl"

setup(
    name=package_name,
    version="0.1",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Wavefire5201",
    maintainer_email="enoch.zhu154@gmail.com",
    description="Multitool package for Roboboat",
    license="GNU GPLv3",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "mhsboat_ctrl = mhsboat_ctrl.mhsboat_ctrl:main"
        ],
    },
)
