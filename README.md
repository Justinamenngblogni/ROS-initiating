# ROS2 Initiating - Politecnico di Torino Onboarding

This repository contains my progress on the official ROS2 (Jazzy) tutorials, acting as my initial onboarding workspace for the STREAMRobotics lab.

## 🎯 Objectives
The goal of this workspace is to master the core concepts of ROS2, including:
- CLI Tools (Nodes, Topics, Services, Actions)
- Client Libraries (Python)
- Creating and building packages using `colcon`
- Developing Publisher/Subscriber nodes
- Defining custom interfaces (`.msg`, `.srv`)

## 🛠️ Environment & Prerequisites
- **OS:** xubuntu 24.04 (via Virtual Machine)
- **ROS2 Distribution:** Jazzy
- **Language:** Python 3

## 📁 Workspace Structure
This repository focuses strictly on the `src/` directory. 
Current packages implemented:
- `cpp_pubsub` : Basic C++ implementation of publisher and subscriber nodes.
- `cpp_srvcli` : Basic C++ implementation of a service and client node pair.
- `my_package_C_justin` : Personal test package for experimenting with C++ node creation and custom logic.
- `my_package_python_justin` : Personal test package for experimenting with Python node creation and custom logic.
- `py_pubsub` : Basic Python implementation of publisher and subscriber nodes.
- `ros_tutorials` : Reference folder containing official ROS 2 tutorial example packages.
- `tutorial_interfaces` : Custom package for defining message (`.msg`) and service (`.srv`) interfaces for use in tutorials.

## 🚀 How to build and run
To test the nodes in this repository, clone it into your local workspace and build it:

```bash
# Clone the repository into your workspace's src folder
git clone [https://github.com/Justinamenngblogni/ROS-initiating.git](https://github.com/Justinamenngblogni/ROS-initiating.git) src

# Build the all packages
colcon build --symlink-install

# Source the setup file
source install/setup.bash


# Run the publisher  nodes for example
ros2 run  cpp_pubsub talker

# Run the subscriber nodes for example
ros2 run  cpp_pubsub listener