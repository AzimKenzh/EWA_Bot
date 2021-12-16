import React from 'react'
import {
  CCol,
  CContainer,
  CRow
} from '@coreui/react'
import CIcon from "@coreui/icons-react";


const NoItems = (props) => {

  return (
    <>
      <CContainer>
        <CRow className="justify-content-center">
          <CCol md="6" className="mt-5 mb-5">
            <div className="d-flex flex-column align-items-center">
              <CIcon name="cilMagnifyingGlass"  size={'5xl'}/>
              <p className="text-muted text-center ">{props.title}</p>
            </div>
          </CCol>
        </CRow>
      </CContainer>
    </>
  )
}

export default NoItems
