from abc import ABC, abstractmethod

class NetworkDevice(ABC):

    def __init__(self, hostname, ip_address, uptime_hours):
        self.hostname = hostname
        self.ip_address = ip_address
        self.uptime_hours = uptime_hours

    # Protected attribute
        self._connection_status = False

    # Private attribute
        self._last_backup_time = None

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def backup_config(self):
        pass

    def reboot(self):
        print(f"{self.hostname} is rebooting")

# Special Methods
    def __str__(self):
        return f"{self.hostname}: {self.ip_address} - Uptime hours: {self.uptime_hours}"

    def __repr__(self):
        return f"{self.hostname}, {self.ip_address}, {self.uptime_hours}"

    def __eq__(self, other):
        if isinstance(other, NetworkDevice):
            return (self.hostname == other.hostname and self.ip_address == other.ip_address)

    def __lt__(self):
        if isinstance(other, NetworkDevice):
            return self.uptime_hours < other.uptime_hours
        return NotImplemented

# Router Subclass
class Router(NetworkDevice):
    def __init__(self, hostname, ip_address, uptime_hours, routing_protocol):
        super().__init__(hostnmame, ip_address, uptime_hours)
        self.routing_protocol = routing_protocol

    def connect(self):
        self.connection_status = true
        print(f"{self.hostname} is connected!")

    def backup_config(self):
        self.update_backup_time = True
        print(f"{self.hostname} is backing up!")
        return true

    def __str__(self):
        return (f"Router: {self.hostname} | IP address: {self.ip_address} | " 
                f"Uptime (hours): {self.uptime_hours} | Routing Protocol: {self.routing_protocol}")

# Switch Subclass
class Switch(NetworkDevice):
    def __init__(self, hostname, ip_address, uptime_hours, vlan_count):
        super().__init__(hostname, ip_address, uptime_hours)
        self.vlan_count = vlan_count

    def connect(self):
        self.connection_status = true
        print(f"{self.hostname} is connected!")

    def backup_config(self):
        self.update_backup_time = True
        print(f"{self.hostname} is backing up!")
        return true
    
    def __str__(self):
        return (f"Router: {self.hostname} | IP address: {self.ip_address} | "
                f"Uptime (hours): {self.uptime_hours} | Vlan Count: {self.vlan_count} ")

#Polymorphic Function
def backup_all_devices(devices):
    successful_backups = 0

    for device in devices:
        if isinstance(device, NetworkDevice):
            if device.backup_config():
                successful_backups += 1

    return successful_backups

# Testing

# Create 2 Routers
router1 = Router("Router1", "10.0.0.1", 120, "OSPF")
router2 = Router("Router2", "10.0.0.2", 75, "BGP")

# Create 2 Switches
switch1 = Switch("Switch1", "10.0.1.1", 200, 24)
switch2 = Switch("Switch2", "10.0.1.2", 50, 48)

# Add to a list
devices = [router1, router2, switch1, switch2]

# Call backup_all_devices()
print("\n=== Backing Up Devices ===")
backup_count = backup_all_devices(devices)
print(f"\nSuccessful backups: {backup_count}")

# Sort devices by uptime
devices.sort()

# Print sorted list
print("\n=== Devices Sorted by Uptime ===")
for device in devices:
    print(device)
