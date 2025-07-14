# CARLA API Test

This is a minimal Python script to test the CARLA simulator API.

## Features

- Connects to CARLA server (`localhost:2000`)
- Enables **synchronous mode** with fixed delta time (20 FPS)
- Runs a basic simulation tick loop
- Includes commented code to spawn a vehicle and enable autopilot

## Requirements

- CARLA Simulator running
- `carla` Python API installed

## Usage

```bash
python3 carla_test.py
