import asyncio
from core.photon import Photon


photon = Photon()

async def main():
    await photon.connect()
    
    
if __name__ == "__main__":
    asyncio.run(main())