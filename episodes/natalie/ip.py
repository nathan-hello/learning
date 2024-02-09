import ipaddress
import ipwhois
import sqlite3
import asyncio
from dataclasses import dataclass
from typing import Coroutine
import time

import concurrent.futures as cf


@dataclass
class IpInfo:
    ip_str: str
    cidr: str
    asn: str
    name: str
    country: str
    city: str
    owner: str


# Function to create the database table
def create_table():
    conn = sqlite3.connect("whois_database.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS whois_data
                 (ip_address TEXT PRIMARY KEY, cidr TEXT, asn TEXT, name TEXT, country TEXT, city TEXT, owner TEXT)"""
    )
    conn.commit()
    conn.close()


# Function to insert data into the database
def insert_data(ip: IpInfo):
    if ip == None:
        print(f"ip in insert_data: {ip}")
        return
    conn = sqlite3.connect("whois_database.db")
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO whois_data (ip_address, cidr, asn, name, country, city, owner) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (ip.ip_str, ip.cidr, ip.asn, ip.name, ip.country, ip.city, ip.owner),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        # Skip if there's a unique constraint violation
        pass
    finally:
        conn.close()




# Function to query WHOIS information for an IP address
def get_whois_sync(ips):
    def __run(ip):
        obj = ipwhois.IPWhois(ip)
        result = obj.lookup_whois()
        if "nets" in result:
            net_info = result["nets"][0]
            n = IpInfo(
                ip,
                net_info.get("cidr"),
                net_info.get("asn"),
                net_info.get("name"),
                net_info.get("country"),
                net_info.get("city"),
                net_info.get("description"),
            )
            insert_data(n)
            # print(n)

    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        pool.map(__run, [str(ip) for ip in ips])


async def get_whois_async(ips):
    async def __run(ip):
        obj = ipwhois.IPWhois(ip)
        result = obj.lookup_whois()
        if "nets" in result:
            net_info = result["nets"][0]
            n = IpInfo(
                ip,
                net_info.get("cidr"),
                net_info.get("asn"),
                net_info.get("name"),
                net_info.get("country"),
                net_info.get("city"),
                net_info.get("description"),
            )
            insert_data(n)
            print(n)
    promises: list[Coroutine] = []

    for ip in ips:
        promises.append(__run(str(ip)))

    print(f"made {len(promises)} promises")
    await asyncio.gather(*promises)


# Main function to loop over IPv4 addresses and insert WHOIS data into the database
async def main():
    print("starting")
    create_table()
    dns_resolver_ranges = [
        ipaddress.IPv4Network("8.8.8.0/24"),  # Google Public DNS
        ipaddress.IPv4Network("1.1.1.0/24"),  # Cloudflare DNS
        # Add more DNS resolver ranges if needed
    ]
    print(f"{len(dns_resolver_ranges)} dns resolver ranges")

    ips = [ip for ip in ipaddress.IPv4Network("0.0.0.0/0") if ip.is_private == False]
    print(f"{len(ips)} ips in all_ips before stripping private")

    ips = [ip for ip in ips if ip not in dns_resolver_ranges]
    print(f"{len(ips)} ips in all_ips after stripping private")

    start = time.time()
    get_whois_sync(ips)
    # await get_whois_async(ips)
    end = time.time()
    print(f"done in {end - start} seconds")


if __name__ == "__main__":
    asyncio.run(main())
