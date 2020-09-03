from sqlalchemy import Column, String, Integer, Float, Time
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# 定义 Pvc 对象:
class RmsPvc(Base):
    def to_dict(self):
        return {c.name: getattr(self, c.name, None)
                for c in self.__table__.columns}
    # 表的名字:
    __tablename__ = 'rms_pvc'
    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    namespace = Column(String(50))
    capacity = Column(String(50))
    disk_type = Column(String(50))
    mode = Column(String(50))
    storage_class = Column(String(50))
    module = Column(String(50))
    ou_id = Column(String(50))
    ou_name = Column(String(50))
    is_delete = Column(Integer)
    cre_user = Column(String(50))
    cre_date = Column(String(50))
    upd_user = Column(String(50))
    upd_date = Column(String(50))
