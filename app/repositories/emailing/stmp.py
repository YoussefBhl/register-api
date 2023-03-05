import asyncio
from typing import Callable

async def mock_stmp(code) -> Callable:
    await asyncio.sleep(1)
    print(f"{8*'*'} Mock STMP Server {8*'*'}")
    print(f"{8*'*'} Code: {code} {8*'*'}")