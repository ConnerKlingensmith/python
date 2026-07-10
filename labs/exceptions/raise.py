def validate_port(port):
    if not (1 <= port <= 65535):
        raise ValueError("Port must be between 1 and 65535")
    return port
