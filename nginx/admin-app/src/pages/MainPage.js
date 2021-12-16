import {lazy, useEffect, useState} from "react";
import {CDataTable,CBadge,CButton,CCollapse,CCardBody,CCol, CRow,CTextarea, CCard} from "@coreui/react";
import CIcon from "@coreui/icons-react";
import {useDispatch, useSelector} from "react-redux";
import {getAllItems} from "../redux/actions/mainActions";
import FullSpinner from "../components/spinners/FullSpinner";
const Modal =  lazy(() => import('../components/modal/ProductParsingResults'));

export default function MainPage({pageName}){

  //STATES
  const dispatch = useDispatch()
  const {listItems,loading} = useSelector(state => state.amazon)
  const [details, setDetails] = useState([])
  const [showModal, setShowModal] = useState(false)
  const [editActive, setEditActive] = useState(false)
  const [activeIndex, setActiveIndex] = useState(null)
  const [inputValue, setInputValue ] = useState("")

  //FETCH_DATA
  useEffect(() => {
    dispatch(getAllItems(pageName+'_admin'))
  },[pageName])

  const toggleDetails = (index) => {
    const position = details.indexOf(index)
    let newDetails = details.slice()
    if (position !== -1) {
      newDetails.splice(position, 1)
    } else {
      newDetails = [...details, index]
    }
    setDetails(newDetails)
  }

  //TABLE
  const fields = [
    { key: 'title', _style: { width: '70%'}, label: 'Title' },
    { key: 'edit', label:''},
    {
      key: 'show_details',
      label: '',
      sorter: false,
      filter: false
    },
    { key:'delete', label: ''},
    { key: 'status', lable:'Status'},
    { key: 'registered', label: 'Date'  },
    { key:'link', label: 'Link'}
  ]

  const getBadge = (status)=>{
    switch (status) {
      case 'Active': return 'success'
      case 'Inactive': return 'secondary'
      case 'Pending': return 'warning'
      case 'Banned': return 'danger'
      default: return 'primary'
    }
  }
  if (loading) {
    return <FullSpinner/>
  }

  return (
    <CRow className={"mt-2"}>
      <CCol>
        <CCard className={'main-wrapper'}>
          <Modal showModal={showModal} setShowModal={setShowModal}/>

          <CDataTable
            items={listItems}
            fields={fields}
            footer
            itemsPerPage={8}
            hover
            sorter
            pagination
            scopedSlots = {{
              'title':
                (item, index)=>(
                  <td key={item.id}>
                    <CTextarea value={item.title || inputValue} onChange={e => setInputValue(e.target.value)} disabled={(item.id === activeIndex && editActive) ? false:true}/>
                  </td>
                ),
              'edit':(item, index) => (<td key={item.id}> <CIcon onClick={() => {
                setEditActive(!editActive)
                setActiveIndex(item.id)
              }} role={'button'} size={'xl'} className={'row text-warning'} name={'cilPencil'}/></td>),
              'show_details':
                (item, index) => {
                  return (
                    <td className="">
                      <CIcon role={'button'} size={'xl'} className={'row'} name={'cilFullscreen'} onClick={() => setShowModal(true)}/>
                    </td>
                  )
                },
              'delete':(item, index ) => <td><CIcon role={'button'} size={'xl'} className={'row text-danger'} name={'cilTrash'} onClick={toggleDetails.bind(null,index)}/></td>,
              'link':item =>               <td>    <a href={item.url} target="_blank">link</a></td>,
              'registered':
                (item)=>(
                  <td key={item.id}>
                    <p>01.10.2021</p>
                  </td>
                ),
              'status':
                (item)=>(
                  <td>
                    <CBadge color={getBadge('Active')}>
                      {"Pending"}
                    </CBadge>
                  </td>
                ),

              'details':
                (item, index)=>{
                  return (
                    <CCollapse show={details.includes(index)}>
                      <CCardBody>
                        <h4>
                          {item.title}
                        </h4>
                        <p className="text-muted">Date: 01.01.2021</p>
                        <CButton size="sm" color="info" onClick={toggleDetails.bind(null,index)}>
                          Close
                        </CButton>
                        <CButton size="sm" color="danger" className="ml-1">
                          Delete
                        </CButton>
                      </CCardBody>
                    </CCollapse>
                  )
                }
            }}
          />

        </CCard>

      </CCol>
    </CRow>
  )
}
