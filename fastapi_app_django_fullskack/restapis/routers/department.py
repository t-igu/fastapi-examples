from datetime import datetime
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from restapis.db_utils import execute_query
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import (
    Table, Column, MetaData, Integer, Sequence, String, DATETIME, text
)

metadata = MetaData()

t_department = Table(
    "t_department",
    metadata,
    Column('id', Integer, Sequence('t_department_id_seq'), primary_key=True),
    Column('name', String, nullable=False),
    Column('created_at', DATETIME, nullable=False, server_default=current_timestamp()),
    Column('updated_at', DATETIME, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
)

router = APIRouter()

@router.get('')
async def t_departments_get():
    query = str(t_department.select())
    data = await execute_query(query)
    # print("data", data)
    return ORJSONResponse(data)
