def read_server_port(filename, server_name):
    """Read server port from config file"""
    try:
        # Open file
        with open(filename, "r") as f:
            import json
            config = json.load(f)
        
        # Get server config
        server = config[server_name]
        
        # Get port
        port = int(server["port"])
        
        return port
    
    except FileNotFoundError:
        print(f"Config file '{filename}' not found")
        return 8080  # Default port
    
    except KeyError as e:
        print(f"Server or key not found: {e}")
        return 8080
    
    except ValueError:
        print("Port is not a valid number")
        return 8080
    
    except json.JSONDecodeError:
        print("Invalid JSON in config file")
        return 8080

# Test it
port = read_server_port("servers.json", "web-1")
print(f"Using port: {port}")
