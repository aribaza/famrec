class Room:
    def __init__(self, name, capacity, occupants, connections):
        self.name = name
        self.capacity = capacity
        self.occupants = occupants
        self.connections = connections

    def is_overfull(self):
        return len(self.occupants) > self.capacity

# Define the maze structure using Room objects
maze = {
    "living_room": Room(
        name="Living Room",
        capacity=2,
        occupants=["Graham"],
        connections={
            "outside": "garden",
            "upstairs": "bedroom",
            "north": "kitchen"
        }
    ),
    "kitchen": Room(
        name="Kitchen",
        capacity=1,
        occupants=[],
        connections={
            "south": "living_room"
        }
    ),
    "garden": Room(
        name="Garden",
        capacity=3,
        occupants=["David","Ari","Sara","Christian"],
        connections={
            "inside": "living_room"
        }
    ),
    "bedroom": Room(
        name="Bedroom",
        capacity=2,
        occupants=[],
        connections={
            "downstairs": "living_room",
            "jump_out": "garden"  # Jumping out of the window to the garden
        }
    )
}

# Example of accessing the maze structure and checking for overfull rooms
for room_key, room in maze.items():
    print(f"Place: {room.name}")
    print(f"  Capacity: {room.capacity}")
    print(f"  Occupants: {', '.join(room.occupants) if room.occupants else 'None'}")
    print(f"  Connections: {', '.join(room.connections.keys())}")
    print(f"  Overfull: {'Yes' if room.is_overfull() else 'No'}")
    print()

# Calculate total people and limit
total_people = sum(len(room.occupants) for room in maze.values())
total_capacity = sum(room.capacity for room in maze.values())

print(f"Total number of people in the maze: {total_people}")
print(f"Total possible occupants in the maze: {total_capacity}")

# Print rooms that are overfull
overfull_rooms = {room_key: len(room.occupants) for room_key, room in maze.items() if room.is_overfull()}
print("Overfull rooms:", overfull_rooms)
