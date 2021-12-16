import React, { useState} from 'react'
import {useHistory} from "react-router-dom"
import {
  CButton,
  CCard,
  CCardBody,
  CTabs,
  CNav,
  CNavItem,
  CNavLink,
  CTabContent,
  CTabPane,
  CCardHeader,
} from "@coreui/react"
import CategoryCreateUpdateDeleteModal from "../components/modal/createUserModal";
import {CATEGORY_MODAL_TYPE} from "../helpers/constants";
import {OperatorInfo} from "../components/OperatorInfo";

export const CreateUser = () => {
  const history = useHistory()
  const [modal, setModal] = useState({
    isOpen: false,
    item: null,
    modalType: CATEGORY_MODAL_TYPE.DELETE,
    title: ''
  })
  const setModalHandler = (newModalOption) => {
    setModal(() =>  newModalOption)
  }

  return (
    <>

      <CCard className="m-5">

        <CCardHeader>
          <CButton
            color="secondary"
            style={{width: "100px", margin: "10px"}}
            onClick={() => history.goBack()}
          >
            НАЗАД
          </CButton>
        </CCardHeader>
        <CCardBody>
          <CTabs activeTab="operator">
            <CNav variant="tabs">
              <CNavItem>
                <CNavLink data-tab="operator">
                  Операторы
                </CNavLink>
              </CNavItem>
            </CNav>
            <CTabContent>
              <CTabPane data-tab="operator">
                <OperatorInfo setModalHandler={setModalHandler}/>
              </CTabPane>
            </CTabContent>
          </CTabs>
        </CCardBody>
        <CategoryCreateUpdateDeleteModal
          isOpen={modal.isOpen}
          item={modal.item}
          title={modal.title}
          modalType={modal.modalType}
          setModal={setModal}
        />
      </CCard>

    </>
  );
};




