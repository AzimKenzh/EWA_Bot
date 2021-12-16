import React, {useState} from 'react'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import {
  CButton,
  CCard,
  CCardBody,
  CCardFooter,
  CCol,
  CContainer,
  CForm,
  CInput,
  CInputGroup,
  CInputGroupPrepend,
  CInputGroupText,
  CRow
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
import {useDispatch} from "react-redux";
import {signUp} from "../redux/actions/authActions";

const RegisterPage = () => {
  const dispatch = useDispatch()
  const [userData, setUserData] = useState({
    username:'',
    password: ''
  })
  const [repeatPassword, setRepeatPassword] = useState('')

  const changeUserDataHandler = (e) => {
    setUserData((prev) => ({
      ...prev,
        [e.target.name]: e.target.value
    }))
  }
  const submitHandler = () => {
    if (repeatPassword === userData.password) {
      toast('created')
    } else {
      toast.error('error')
    }

  }

  return (
    <div className="c-app c-default-layout flex-row align-items-center">
      <CContainer>
        <CRow className="justify-content-center">
          <CCol md="9" lg="7" xl="6">
            <CCard className="mx-4">
              <CCardBody className="p-4">
                <CForm>
                  <h1>Register</h1>
                  <p className="text-muted">Create your account</p>
                  <CInputGroup className="mb-3">
                    <CInputGroupPrepend>
                      <CInputGroupText>
                        <CIcon name="cil-user" />
                      </CInputGroupText>
                    </CInputGroupPrepend>
                    <CInput name={'username'} type="text" placeholder="Username" autoComplete="username" value={userData.username} onChange={changeUserDataHandler}/>
                  </CInputGroup>
                  {/*<CInputGroup className="mb-3">*/}
                  {/*  <CInputGroupPrepend>*/}
                  {/*    <CInputGroupText>@</CInputGroupText>*/}
                  {/*  </CInputGroupPrepend>*/}
                  {/*  <CInput type="text" placeholder="Email" autoComplete="email" />*/}
                  {/*</CInputGroup>*/}
                  <CInputGroup className="mb-3">
                    <CInputGroupPrepend>
                      <CInputGroupText>
                        <CIcon name="cil-lock-locked" />
                      </CInputGroupText>
                    </CInputGroupPrepend>
                    <CInput name={'password'} type="password" placeholder="Password" autoComplete="new-password" value={userData.password} onChange={changeUserDataHandler}/>
                  </CInputGroup>
                  <CInputGroup className="mb-4">
                    <CInputGroupPrepend>
                      <CInputGroupText>
                        <CIcon name="cil-lock-locked" />
                      </CInputGroupText>
                    </CInputGroupPrepend>
                    <CInput type="password" placeholder="Repeat password" autoComplete="new-password" value={repeatPassword} onChange={(e) => setRepeatPassword(e.target.value)}/>
                  </CInputGroup>
                  <ToastContainer autoClose={3000}/>
                  <CButton color="success" block onClick={submitHandler}>Create Account</CButton>
                </CForm>
              </CCardBody>
              {/*<CCardFooter className="p-4">*/}
              {/*  <CRow>*/}
              {/*    <CCol xs="12" sm="6">*/}
              {/*      <CButton className="btn-facebook mb-1" block><span>facebook</span></CButton>*/}
              {/*    </CCol>*/}
              {/*    <CCol xs="12" sm="6">*/}
              {/*      <CButton className="btn-twitter mb-1" block><span>twitter</span></CButton>*/}
              {/*    </CCol>*/}
              {/*  </CRow>*/}
              {/*</CCardFooter>*/}
            </CCard>
          </CCol>
        </CRow>
      </CContainer>
    </div>
  )
}

export default RegisterPage
