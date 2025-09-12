from app.model.v1.meja.meja_schemas import MejaCreate, MejaUpdate, MejaResponse

# Penyimpanan sementara (simulasi database)
_meja_db: list[MejaResponse] = []
_id_counter = 1

""" Service functions untuk meja """
def get_all_meja():
    return _meja_db

""" Helper function untuk mendapatkan meja berdasarkan ID """
def get_meja_by_id(meja_id: int):
    for meja in _meja_db:
        if meja.id == meja_id:
            return meja
    return None

""" Function untuk menambah meja baru  """
def create_meja(meja: MejaCreate):
    global _id_counter
    new_meja = MejaResponse(id=_id_counter, **meja.model_dump())
    _meja_db.append(new_meja)
    _id_counter += 1
    return new_meja

""" Function untuk mengupdate data meja   """
def update_meja(meja_id: int, meja_update: MejaUpdate):
    meja = get_meja_by_id(meja_id)
    if not meja:
        return None
    """ Update fields yang diubah """
    update_data = meja_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(meja, key, value)

    return meja

""" Function untuk menghapus meja """
def delete_meja(meja_id: int):
    global _meja_db
    meja = get_meja_by_id(meja_id)
    if not meja:
        return None

    _meja_db = [m for m in _meja_db if m.id != meja_id]
    return meja
