# python3-tapo - Debian Package

This repository contains the Debian packaging files for the [Tapo Python library](https://pypi.org/project/tapo/) - an unofficial API client for TP-Link Tapo smart devices.

## About Tapo

Tapo is a Rust-based Python library that provides an API client for controlling TP-Link Tapo smart devices. It supports a wide range of devices including:

- **Light bulbs**: L510, L520, L530, L535, L610, L630
- **Light strips**: L900, L920, L930  
- **Smart plugs**: P100, P105, P110, P110M, P115
- **Power strips**: P300, P304M, P316M
- **Hubs**: H100
- **Switches**: S200B
- **Sensors**: KE100, T100, T110, T300, T310, T315

## Package Information

- **Package Name**: `python3-tapo`
- **Version**: 0.8.4-1
- **Architecture**: amd64
- **Section**: python
- **Priority**: optional
- **License**: MIT

## Dependencies

- Python 3.13+
- libc6 (>= 2.34)
- libgcc-s1 (>= 4.2)

## Automated CI/CD

This package includes a Jenkins pipeline (`debian/Jenkinsfile`) that:

1. **Automatically detects** the latest version from PyPI
2. **Downloads** the current wheel from PyPI  
3. **Updates** `debian/changelog` with the new version
4. **Updates** `setup.py` with the current version
5. **Builds** packages for multiple distributions:
   - Debian Trixie
   - Debian Forky
   - Ubuntu Jammy
   - Ubuntu Noble
6. **Tests** package installation
7. **Archives** the built packages

## Manual Building

To build the Debian package manually:

```bash
# Install build dependencies
sudo apt update
sudo apt install -y debhelper dh-python python3-all python3-setuptools python3-pip python3-wheel

# Build the package (sources will be downloaded automatically)
dpkg-buildpackage -us -uc -b
```

This will:
1. Download the latest tapo wheel from PyPI
2. Extract the wheel contents
3. Create the Debian packages:
   - `python3-tapo_X.Y.Z-1_amd64.deb` - Main package
   - `python3-tapo-dbgsym_X.Y.Z-1_amd64.deb` - Debug symbols

## Installation

Install the generated package:

```bash
sudo dpkg -i python3-tapo_0.8.4-1_amd64.deb
```

## Usage

After installation, you can use the library in Python:

```python
import tapo

# Create API client
client = tapo.ApiClient("username", "password")

# Connect to a device (example with P110 smart plug)
device = await client.p110("192.168.1.100")

# Control the device
await device.on()
await device.off()

# Get device information
info = await device.get_device_info()
print(info)
```

## Files Structure

- `debian/` - Debian packaging files
  - `control` - Package metadata and dependencies
  - `copyright` - License information
  - `changelog` - Version history (auto-updated by Jenkins)
  - `rules` - Build rules with dynamic source download
  - `source/format` - Source format specification
  - `Jenkinsfile` - Automated CI/CD pipeline
- `setup.py` - Python setup script (version auto-updated)
- Source files are downloaded automatically during build

## Upstream Information

- **Homepage**: https://github.com/mihai-dinculescu/tapo
- **PyPI**: https://pypi.org/project/tapo/
- **Author**: Mihai Dinculescu <mihai.dinculescu@outlook.com>

## Packaging Maintainer

- **Maintainer**: Vitex Software <info@vitexsoftware.com>
- **Repository**: https://github.com/Spoje-NET/python3-tapo

## License

This packaging is released under the MIT License, same as the upstream project.
