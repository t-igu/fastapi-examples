from datetime import datetime
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from apis.db_utils import execute_query
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import (
    Table, Column, MetaData, Integer, Sequence, String, DATETIME, text
)

metadata = MetaData()

employee = Table(
    "t_employee",
    metadata,
    Column('id', Integer, Sequence('t_employee_id_seq'), primary_key=True),
    Column('name', String, nullable=False),
    Column('birthday', DATETIME, default=datetime.now, nullable=False),
    Column('department_id', Integer,),
    Column('created_at', DATETIME, nullable=False, server_default=current_timestamp()),
    Column('updated_at', DATETIME, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
)

router = APIRouter()

@router.get('')
async def employee_get():
    query = str(employee.select())
    data = await execute_query(query)
    # print("data", data)
    return ORJSONResponse(data)
