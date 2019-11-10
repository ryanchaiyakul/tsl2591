import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tsl2591",
    version="0.0.2",
    author="Ryan Chaiyakul",
    description="tsl2591 python driver for stickytoe framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryanchaiyakul/sht3x",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['Adafruit-Blinka==3.0.0',
                      'adafruit-circuitpython-busdevice==4.0.0',
                      'adafruit-circuitpython-tsl2591==1.1.3',
                      'Adafruit-PlatformDetect==1.3.4',
                      'Adafruit-PureIO==0.2.3',
                      'stickytoe_device>=0.0.2',
                      ],
)
