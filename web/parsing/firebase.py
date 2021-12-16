# # Санжар Байке SP, [15/12/21 19:18]
# from typing import List
#
# import firebase_admin
# from firebase_admin import firestore, credentials
# from core.config import settings
#
# certificate_location = '/app/secrets/smartpostdriver-firebase-adminsdk-g5e6c-c55a778cd3.json'
# cred = credentials.Certificate(certificate_location)
# firebase_admin.initialize_app(cred)
# DB = firestore.client()
# FIREBASE_KEY = DB.collection('key')
#
#
# def get_couriers_collection():
#     # different collections for production and testing
#     # if settings.environment == 'production':
#     #     return DB.collection('production')
#     # else:
#     return DB.collection('testing')
#
#
# def get_firebase_key():
#     document = FIREBASE_KEY.document('key').get()
#     fs_key = document.get('key')
#     return fs_key
#
#
# def create_courier_document(courier_id: int):
#     try:
#         document_name = f'courier_{courier_id}'
#         document = get_couriers_collection().document(document_name)
#         document.set({UPDATE_LIST: False, ORDER_CHANGED: 0, NEW_APPOINTMENT: 0, APPOINTMENT_REMOVED: 0})
#     except Exception as e:
#         print(e)
#     return
#
#
# def update_courier_f_key(courier_id: int, key, value):
#     try:
#         document_name = f'courier_{courier_id}'
#         document = get_couriers_collection().document(document_name)
#         if not document.get().exists:
#             create_courier_document(courier_id)
#         document.update({key: value})
#     except Exception as e:
#         print(e)
#     return
#
#
# def update_courier_f_keys_bulk(courier_ids: List[int], key, value):
#     try:
#         batch = DB.batch()
#         data = {key: value}
#         collection = get_couriers_collection()
#         for courier_id in courier_ids:
#             document = collection.document(f'courier_{courier_id}')
#             if not document.get().exists:
#                 create_courier_document(courier_id)
#             batch.update(document, data)
#         batch.commit()
#     except Exception as e:
#         print(e)
#     return