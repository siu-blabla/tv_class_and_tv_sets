# Import the tv class
from tv import TV
from pyfiglet import Figlet

# Create new object
tv1 = TV()
tv2 = TV()

# Set the channel of tv1 to 30
tv1.set_channel(30)

# Set the volume of tv1 to 3
tv1.set_volume(3)

# Set the channel of tv2 to 3
tv2.set_channel(3)

# Set the volume of tv2 to 2
tv2.set_volume(2)

# Print the output channel and volume level of tv1 and tv2
print(f"\033[93m\033[1mtv1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")
print(f"tv2's channel is {tv2.get_channel()} and volume level is {tv2.get_volume()}\033[0m")
