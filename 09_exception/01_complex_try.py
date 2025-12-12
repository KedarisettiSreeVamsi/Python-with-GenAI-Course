def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == 'unknown':
            raise ValueError("Don't know the unknown flavour")
    except ValueError as e:
        print(e)
    else:
        print(f"Serving {flavour} chai")
    finally:
        print("Next customer please")

serve_chai("Masala")
serve_chai("unknown")