from contextlib import contextmanager

from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from rms.client.entity.rms_pvc import RmsPvc, Base
from rms.client.storage_conn_pool import StorageConnectPool
from rms.utils import logger


class StorageClient(object):
    @staticmethod
    @StorageConnectPool()
    @contextmanager
    def insert(pvc, service_api: Engine = None):
        try:
            db_session = sessionmaker(bind=service_api)
            session = db_session()
            session.add(pvc)
            yield
            # 提交即保存到数据库:
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            logger.error(e)
        finally:
            if session is not None:
                # 关闭 session:
                session.close()
        return False

    @staticmethod
    @StorageConnectPool()
    @contextmanager
    def delete(namespace, pvc_name, ou_id, service_api: Engine = None):
        try:
            db_session = sessionmaker(bind=service_api)
            session = db_session()
            rows = session.query(RmsPvc).filter(RmsPvc.namespace == namespace, RmsPvc.name == pvc_name,
                                                RmsPvc.is_delete == 0, RmsPvc.ou_id == ou_id).all()
            for row in rows:
                row.is_delete = 1
            yield
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            logger.error(e)
        finally:
            if session is not None:
                # 关闭 session:
                session.close()
        return False

    @staticmethod
    @StorageConnectPool()
    def query(namespace, module, ou_id, service_api: Engine = None):
        try:
            db_session = sessionmaker(bind=service_api)
            session = db_session()
            Base.to_dict = RmsPvc.to_dict
            conditions = [RmsPvc.is_delete == 0, RmsPvc.cre_user == ou_id]
            if namespace is not None:
                conditions.append(RmsPvc.namespace == namespace)
            if module is not None:
                conditions.append(RmsPvc.module == module)
            rows = session.query(RmsPvc).filter(*conditions).all()
            return [row.to_dict() for row in rows]
        except Exception as e:
            logger.error(e)
        finally:
            if session is not None:
                # 关闭 session:
                session.close
        return False
