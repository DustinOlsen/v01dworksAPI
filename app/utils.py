import hashlib
import os
from pathlib import Path
import geoip2.database

# Salt for hashing IP addresses. 
# Created once and stored to maintain consistency across restarts.
SALT_FILE = Path("data/.salt")

def get_salt():
    # Ensure parent directory exists
    SALT_FILE.parent.mkdir(exist_ok=True)
    
    if not SALT_FILE.exists():
        salt = os.urandom(32)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
    with open(SALT_FILE, "rb") as f:
        return f.read()

SALT = get_salt()

def hash_ip(ip_address: str) -> str:
    """
    Hashes an IP address with a salt.
    This ensures we can track uniqueness without storing the actual IP.
    """
    return hashlib.sha256(SALT + ip_address.encode()).hexdigest()

def get_country_from_ip(ip_address: str) -> str:
    """
    Resolves an IP address to a country code using GeoLite2.
    Returns 'Unknown' if database is missing or IP is not found.
    """
    # Check for Country or City database
    db_files = ["GeoLite2-Country.mmdb", "GeoLite2-City.mmdb"]
    db_path = next((f for f in db_files if os.path.exists(f)), None)
    
    if not db_path:
        return "Unknown"

    try:
        with geoip2.database.Reader(db_path) as reader:
            # .country() works for both City and Country databases
            response = reader.country(ip_address)
            return response.country.iso_code or "Unknown"
    except (FileNotFoundError, Exception):
        return "Unknown"
