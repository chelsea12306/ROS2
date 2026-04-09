# ROS2-Based Application Development
A practical robotics project built on Robot Operating System 2 (ROS2), focusing on implementing core ROS2 communication functionalities and integrating computer vision capabilities into a robotics system. The project combines data transmission and real-time face detection to demonstrate ROS2’s versatility and practicality in robotics development scenarios.

## Overview
This project is constructed based on ROS2, covering two core functional modules: topic publishing/subscribing for New Zealand travel logs and real-time face detection. It simulates real-world robotics application scenarios, integrating ROS2 core mechanisms with computer vision technology to showcase the complete process of ROS2 node development, inter-node communication, and system integration.

### Topic Communication Development (New Zealand Travel Log Publishing & Subscribing)
- Implements ROS2 topic communication mechanism, designing and developing a publisher node to release New Zealand travel logs.
- Develops a corresponding subscriber node to receive, parse, and display the published travel log data in real time, ensuring reliable message transmission, and synchronization between publisher and subscriber nodes.


### Face Detection Integration
- Develops a face detection client node based on ROS2, integrating pre-trained computer vision models to capture real-time video input.
- Implements real-time face detection algorithms, identifying human faces in the video stream and extracting key information (face coordinates, confidence scores) from detection results.
