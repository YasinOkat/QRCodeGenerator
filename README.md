# QR Code Generator

This project is a simple QR code generator developed for Movus Logistics. It allows you to generate QR codes for various devices and equipment.

## Features

- Generates QR codes for different types of devices and equipment.
- Supports a range of device categories, including laptops, routers, access points, barcode scanners, and more.
- Provides options for manual entry of custom device codes.
- Generates both small and large QRCode labels based on the device type.
- Utilizes the `qrcode` library for QR code generation.
- Uses the `PIL` (Python Imaging Library) for image manipulation and drawing.
- Customizable font selection for text on generated images.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yasinokat/QRCodeGenerator.git
   cd barcode-qr-generator

2. Install the required dependencies:

   ```bash
   pip install pillow qrcode

## Usage

1. Navigate to the project directory:

   ```bash
   cd qr_code_generator

2. Run the script:

    ```bash
   python qr_code_generator

3. Select the device type or enter a custom code when prompted.

4. Enter the starting and ending numbers for the barcode/QR code range.

5. The script will generate barcode and QR code images for each number in the range and save them in the respective folders.

## License

This project is licensed under the GNU General Public License (GPL). See the LICENSE file for more information.
