# from fastapi import Depends, FastAPI, APIRouter
# from sqlalchemy.future import select
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from app.db import get_session
# from app.models import Song, SongCreate
#
# router = APIRouter()
#
#
# @router.get("/cupons", response_model=list[Song])
# async def get_cupons(session: AsyncSession = Depends(get_session)):
#     result = await session.execute(select(Song))
#     songs = result.scalars().all()
#     return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]
#
#
# @router.post("/cupom")
# async def create_cupom(song: SongCreate, session: AsyncSession = Depends(get_session)):
#     song = Song(name=song.name, artist=song.artist, year=song.year)
#     session.add(song)
#     await session.commit()
#     await session.refresh(song)
#     return song
