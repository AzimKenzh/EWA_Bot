import React, {useEffect, useState} from 'react'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import {
  CButton,
  CCard,
  CCardBody,
  CCardGroup,
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
import {useDispatch, useSelector} from "react-redux";
import {login} from "../redux/actions/authActions";
import MiniSpinner from "../components/spinners/MiniSpinner";
import {useHistory} from "react-router-dom";

const LoginPage = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  const {error, isLoginLoading,isAuth} = useSelector(state => state.auth)
  const [userData, setUserData] = useState({
    username:'',
    password: ''
  })

  const changeUserDataHandler = (e) => {
    setUserData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value
    }))
  }
  const submitHandler = () => {
    if (userData.password.trim() && userData.username.trim()) {
        dispatch(login(userData.username, userData.password, redirectSuccessLogin))
    } else {
      toast.error('invalid username or password')
    }
  }
  useEffect(() => {
    if (error) {
      toast.error(error)
      setUserData(prev => ({...prev, password: ''}))
    }
  },[error])
  const redirectSuccessLogin = () => {
    history.push('/ware')
  }
  return (
    <div className="c-app c-default-layout flex-row align-items-center">
      <CContainer>
        <CRow className="justify-content-center">
          <CCol md="5">
            <CCardGroup>
              <CCard className="p-4">
                <CCardBody>
                  <CForm>
                    <h1>Login</h1>
                    <p className="text-muted">Sign In to your account</p>
                    <CInputGroup className="mb-3">
                      <CInputGroupPrepend>
                        <CInputGroupText>
                          <CIcon name="cil-user" />
                        </CInputGroupText>
                      </CInputGroupPrepend>
                      <CInput type="text" placeholder="Username" autoComplete="username" name={'username'} value={userData.username} onChange={changeUserDataHandler}/>
                    </CInputGroup>
                    <CInputGroup className="mb-4">
                      <CInputGroupPrepend>
                        <CInputGroupText>
                          <CIcon name="cil-lock-locked" />
                        </CInputGroupText>
                      </CInputGroupPrepend>
                      <CInput type="password" placeholder="Password" autoComplete="current-password" name={'password'} value={userData.password} onChange={changeUserDataHandler}/>
                    </CInputGroup>
                    <CRow>
                      <CCol xs="6">
                        <CButton color="primary" className="px-4" onClick={submitHandler}> {isLoginLoading ? <MiniSpinner/> : 'login'} </CButton>
                      </CCol>
                      <CCol xs="6" className="text-right">
                        <CButton color="link" className="px-0">Forgot password?</CButton>
                      </CCol>
                    </CRow>
                  </CForm>
                </CCardBody>
              </CCard>
              {/*<CCard className="text-white bg-primary py-5 d-md-down-none" style={{ width: '44%' }}>*/}
              {/*  <CCardBody className="text-center">*/}
              {/*    <div>*/}
              {/*      <h2>Sign up</h2>*/}
              {/*      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut*/}
              {/*        labore et dolore magna aliqua.</p>*/}
              {/*      <Link to="/register">*/}
              {/*        <CButton color="primary" className="mt-3" active tabIndex={-1}>Register Now!</CButton>*/}
              {/*      </Link>*/}
              {/*    </div>*/}
              {/*  </CCardBody>*/}
              {/*</CCard>*/}
            </CCardGroup>
          </CCol>
        </CRow>
        <ToastContainer autoClose={3000}/>
      </CContainer>
    </div>
  )
}

export default LoginPage
