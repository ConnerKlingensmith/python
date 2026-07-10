def read_config(filename):
    file = None
    try:
        file = open(filename, "r")
        data = file.read()
        return data
    
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    
    finally:
        # This ALWAYS runs
        if file:
            file.close()
            print("File closed")

config = read_config("config.txt")
