import carla
import time

def main():
    # Connect to the CARLA server
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()

    # Get the current world settings
    settings = world.get_settings()

    # Set synchronous mode and fixed delta time
    settings.synchronous_mode = True  # Enable synchronous mode
    settings.fixed_delta_seconds = 0.05  # Simulation steps at 20 FPS (1/0.05 = 20)

    # Apply the modified settings
    world.apply_settings(settings)

    # Start simulation and spawn a vehicle
    # blueprint_library = world.get_blueprint_library()
    # vehicle_bp = blueprint_library.filter('vehicle.*')[0]  # Get any vehicle blueprint
    # spawn_point = world.get_map().get_spawn_points()[0]  # Use the first available spawn point

    # vehicle = world.spawn_actor(vehicle_bp, spawn_point)
    # print(f"Spawned vehicle: {vehicle.type_id}")

    print("updating carla tick ...")
    # world.tick()

    try:
        # Run simulation in synchronous mode
        while True:
            world.tick()  # Step the simulation forward
            # vehicle.set_autopilot(True)
            print("Simulation ticking ...")

            time.sleep(0.1)  # Add a delay for observing the simulation

    except KeyboardInterrupt:
        print("Simulation stopped.")

    # finally:
    #     # Clean up and restore settings
    #     print("Destroying actors...")
    #     vehicle.destroy()
    #     settings.synchronous_mode = False  # Disable synchronous mode
    #     world.apply_settings(settings)

if __name__ == '__main__':
    main()
