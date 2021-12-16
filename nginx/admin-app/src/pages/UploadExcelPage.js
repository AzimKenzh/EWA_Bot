import React, { useState } from 'react'
import {
  CButton,
  CCol,
  CContainer,
  CInput,
  CInputGroup,
  CInputGroupAppend,
  CRow
} from '@coreui/react'
import xlsx from "xlsx";
import { toastify } from "../helpers/toastify";


const UploadExcelPage = () => {
  const [excelData, setExcelData ] = useState([])

  const readUploadFile = (e) => {
    e.preventDefault();
    if (e.target.files) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const data = e.target.result;
        const workbook = xlsx.read(data, { type: "array" });
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const json = xlsx.utils.sheet_to_json(worksheet);
        setExcelData(json.map(x => ({'title': x.Title, 'url': x['URL: Amazon'] }))  )
      };
      reader.readAsArrayBuffer(e.target.files[0]);
    }}

  const postFile = async () => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization:"Token " + localStorage.getItem("amazon_auth_token") },
      body: JSON.stringify(excelData)
    };
    fetch('http://161.35.206.91:8080/product_title/', requestOptions)
          .then(response => {
              if (response.ok) {
                toastify("success", "Succesfully sent")
              } else {
                toastify("error", "Failed to sent")
              }
            })
    .catch(err => console.log(err))}


  return (
    <div className="c-app c-default-layout flex-row align-items-center">
      <CContainer>
        <CRow className="justify-content-center">
          <CCol md="6">
            <CInputGroup className="input-prepend">
              <CInput size="16" type="file" onChange={readUploadFile} placeholder="What are you looking for?" />
              <CInputGroupAppend>
                <CButton color="info" onClick={() => postFile()}>Upload file</CButton>
              </CInputGroupAppend>
            </CInputGroup>
          </CCol>
        </CRow>
      </CContainer>
    </div>
  )
}

export default UploadExcelPage
