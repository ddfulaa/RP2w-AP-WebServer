# RP2w-AP-WebServer
This repository contains a simple example script written in CircuitPython that turns your Raspberry Pi Pico W into a Wi-Fi access point (AP) and serves a basic HTML page to connected clients. This project utilizes the CircuitPython libraries wifi and socketpool to create a standalone web server on the Raspberry Pi Pico W.
Features:

* Configures the Raspberry Pi Pico W to function as a Wi-Fi access point.
* Sets up a socket server to listen for incoming connections on port 80.
* Responds to client requests with a basic HTML page displaying a friendly greeting.

To use this code, make sure you have the CircuitPython firmware and the required libraries (wifi and socketpool) installed on your Raspberry Pi Pico W. Set the environment variables WIFI_SSID and WIFI_PW to your desired SSID and password for the Wi-Fi access point.

Instructions:

1. Install the CircuitPython firmware on your Raspberry Pi Pico W.
2. Install the required CircuitPython libraries wifi and socketpool on the Raspberry Pi Pico W.
3. Set the environment variables WIFI_SSID and WIFI_PW with your desired Wi-Fi access point details.
4. Upload the provided Python script to your Raspberry Pi Pico W.
5. Observe your Raspberry Pi Pico W broadcasting a Wi-Fi access point and serving a simple webpage at its IP address.

This example serves as a starting point for creating more complex projects involving Wi-Fi communication and web serving using CircuitPython on the Raspberry Pi Pico W. Feel free to customize the HTML content and enhance the functionality as needed.

Feel free to modify this description to better fit your repository's purpose and features.
