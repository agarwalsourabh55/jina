from fastapi import APIRouter

from .... import nested_args
from ....models import PeaModel
from ....models.base import StoreItem
from ....stores import partial

router = APIRouter(prefix='/pea', tags=['pea'])
partial_pea_store: partial.PeaStore = partial.PeaStore(nested_args)


@router.get(path='', summary='Get status of a running Pea', response_model=StoreItem)
async def _status():
    return partial_pea_store.status


@router.get(
    path='/arguments',
    summary='Get all accept arguments of a Pea',
)
async def _fetch_pea_params():
    return PeaModel.schema()['properties']


@router.on_event('shutdown')
def _shutdown():
    partial_pea_store.pea.close()