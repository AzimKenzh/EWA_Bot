import React, {useEffect, useState} from "react"
import {CButton, CModal, CModalBody, CModalHeader, CModalFooter, CLabel} from "@coreui/react"
import {CATEGORY_MODAL_TYPE} from "../../helpers/constants"
import {toast} from "react-toastify";

const CategoryCreateUpdateDeleteModal = ({ isOpen, setModal, item, modalType, fetchCategories, title }) => {

  const [input, setInput] = useState({
    username: '',
    password: ''
  })
  const [error, setError] = useState(null)

  useEffect(() => {
    console.log(item)
    if (modalType === CATEGORY_MODAL_TYPE.UPDATE) {
      setInput(prev =>({
        ...prev,
        username: item.first_name,
      }))
    } else {
      setInput({
        username: '',
        password: ''
      })
    }
  }, [item, modalType])

  const onSubmit = async () => {

    if (modalType !== CATEGORY_MODAL_TYPE.DELETE && !input.username.length && !input.password.length) {
      setError('Обязательное поле')
      return
    }

  }




  const onModalClose = () => {
    setModal(false)
    setInput({
      username: '',
      password: ''
    })
  }

  const handleInputChange = e => {
    setInput(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }))
    setError('')
  }

  return (
    <>
      <CModal show={isOpen} onClose={onModalClose}>

        <CModalHeader closeButton>
          { title }
        </CModalHeader>

        {
          modalType === CATEGORY_MODAL_TYPE.DELETE ? <CModalBody className={'text-danger'}>Вы точно хотите удалить?</CModalBody> :
            <CModalBody>
              <CLabel > { 'Username' } </CLabel>
              <input
                className={`form-control ${ error ? 'border-danger' : '' }`}
                type="text"
                name={'username'}
                value={input.username}
                onChange={handleInputChange}
              />
              <CLabel > { 'Password' } </CLabel>
              <input
                className={`form-control ${ error ? 'border-danger' : '' }`}
                name={'password'}
                type="password"
                value={input.password}
                onChange={handleInputChange}
              />
              { error && <CLabel className="text-danger"> { error } </CLabel> }
            </CModalBody>
        }

        <CModalFooter>

          { modalType === CATEGORY_MODAL_TYPE.CREATE && <CButton color='success' onClick={onSubmit}> Создать </CButton> }
          { modalType === CATEGORY_MODAL_TYPE.UPDATE && <CButton color='info' onClick={onSubmit}> Сохранить </CButton> }
          { modalType === CATEGORY_MODAL_TYPE.DELETE && <CButton color='danger' onClick={onSubmit}> Удалить </CButton> }

          <CButton color="secondary" onClick={onModalClose}> Отмена </CButton>

        </CModalFooter>

      </CModal>
    </>
  )
}

export default CategoryCreateUpdateDeleteModal
