from datetime import datetime

def create_filename():
    filename = datetime.now().strftime('%Y%m%d%H%M%S') + str(x)
    return filename
