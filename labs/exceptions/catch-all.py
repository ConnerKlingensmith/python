def risky_operation():
    try:
        # Multiple things that could fail
        data = fetch_data_from_api()
        process_data(data)
        save_to_database(data)

    except ValueError:
        print("Invalid data format")

    except KeyError:
        print("Missing required field")

    except Exception as e:
        # Catches ANYTHING else
        print(f"Unexpected error: {e}")
