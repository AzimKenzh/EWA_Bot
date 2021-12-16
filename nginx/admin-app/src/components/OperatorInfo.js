import React, {useState} from "react";
import {CATEGORY_MODAL_TYPE} from "../helpers/constants";
import {CButton, CDataTable} from "@coreui/react";

export const OperatorInfo = ({setModalHandler}) => {
  const defModalOption = {
    isOpen: true,
    item: null,
    modalType: null,
    title: ''
  }
  const [operators,setOperators] = useState([
    {first_name: "Azamat",
      groups: [2],
      id: 80,
      phone_number: "+996700431223"},
    {first_name: "Marat",
      groups: [2],
      id: 80,
      phone_number: "+996700431223"},
    {first_name: "Samat",
      groups: [2],
      id: 80,
      phone_number: "+996700431223"},
  ])

  const showDeleteModal = () => {
    setModalHandler({
      ...defModalOption,
      modalType: CATEGORY_MODAL_TYPE.DELETE,
    })
  }
  const showUpdateModal = (item) => {
    setModalHandler({
      ...defModalOption,
      modalType: CATEGORY_MODAL_TYPE.UPDATE,
      item
    })
  }
  const showCreateModal = () => {
    setModalHandler({
      ...defModalOption,
      modalType: CATEGORY_MODAL_TYPE.CREATE,
    })
  }

  return (
    <div className="c-body">
      <div className="container-fluid w-100 mt-5">

        <div className="card">
          <div className="card-body">
            <div className='d-flex justify-content-between mb-3'>
              <h3>Операторы</h3>
              <h1><i className="cis-accessible"></i></h1>
              <CButton color="info" onClick={showCreateModal}>
                Добавить оператора
              </CButton>

            </div>

            <CDataTable
              dark={false}
              items={operators}
              fields={fields}
              hover
              sorter
              pagination
              scopedSlots={{
                'name':
                  (item) => (
                    <td>
                      <span className='btn'> {item.name}</span>
                    </td>
                  ),
                'edit':
                  (item) => (
                    <td>
                      <CButton color="primary" onClick={showUpdateModal.bind(null, item)}>
                        Редактировать
                      </CButton>
                    </td>
                  ),
                'delete':
                  (item) => (
                    <td>
                      <CButton color="danger" onClick={showDeleteModal}>
                        Удалить
                      </CButton>
                    </td>
                  ),
              }}
            />
          </div>
        </div>
      </div>

    </div>
  )
}

const fields = [
  {key: 'id', label: "ID", _style: {width: '5%'}},
  {key: 'phone_number', label: "Телефон", _style: {width: '30%'}},
  {key: 'first_name', label: "Имя", _style: {width: '30%'}},
  {key: 'edit', label: "Изменить", _style: {width: '20%'}},
  {key: 'delete', label: "Удалить", _style: {width: '20%'}},
]
