import {lazy, useEffect, useState} from "react"
import {CDataTable,CBadge,CButton,CCol, CInput,CTextarea,CRow,  CCard} from "@coreui/react"
import CIcon from "@coreui/icons-react"
import {useDispatch, useSelector} from "react-redux"
import FullSpinner from "../components/spinners/FullSpinner"
import { getAllItems } from "../redux/actions/mainActions"
import { formatDate } from "../function/Functions"
import { searchSuccess } from "../redux/products/actions"
import { toastify } from "../helpers/toastify";
import { useModalState} from "../helpers/Modals";


const ProductParsingResults =  lazy(() => import('../components/modal/ProductParsingResults'));

export default function WarePage({pageName}){

  //STATES
  const dispatch = useDispatch()
  const {isOpen, onToggle} = useModalState()
  const [showModal, setShowModal] = useState(false)
  const [selectedProduct, setSelectedProduct] = useState(null)
  const [inputValue, setInputValue ] = useState("")
  const [parsing, setParsing] = useState(false)
  const [parsingResults, setParsingResults] = useState({})

  //SELECTOR
  const { title } = useSelector(state => state.searchTitle)
  const {listItems,loading} = useSelector(state => state.amazon)

  //FETCH_PRODUCT
  useEffect(async () => {
    dispatch(getAllItems(title))
  },[title])

  //DELETE_PRODUCT
  async function deleteProductItem(productId){
    const options = {
      method:"DELETE",
      headers:{ Authorization: "Token " + window.localStorage.getItem("amazon_auth_token")}
    }
   await fetch(`http://161.35.206.91:8080/product_title/${productId}/`, options)
      .then(response => {
        if(!response.ok){
          const data = response.json()
          const error = (data && data.message) || response.status
          toastify("error", "Failed to delete")
          return Promise.reject(error)

        }
        toastify("success", "Successfully deleted")
        dispatch(getAllItems(title))
      })
     .catch(error => console.log("There was an error:", error))
  }

  //UPDATE_PRODUCT
  async function updateProductItem(productId){
    await fetch(`http://161.35.206.91:8080/product_title/${productId}/`,{
      method:"PATCH",
      headers:{ "Content-Type":"application/json", Authorization: "Token " + window.localStorage.getItem("amazon_auth_token")},
      body:JSON.stringify({title:inputValue, status:2})
    })
      .then(response => {
        if(!response.ok){
          const data = response.json()
          const error = (data && data.message) || response.status
          return Promise.reject(error)
        }

      })
      .catch(error => console.log("There was an error:", error))
  }

  //PARSE_PRODUCT
  async function parseProductItem(productId){
    setParsing(true)
    await fetch(`http://161.35.206.91:8080/product_title/${productId}/parse/`,{
      method:"POST",
      headers:{ "Content-Type":"application/json", Authorization: "Token " + window.localStorage.getItem("amazon_auth_token")},
      body:JSON.stringify()
    })
      .then(response => {
        if(!response.ok){
          const data = response.json()
          const error = (data && data.message) || response.status
          return Promise.reject(error)
        }
      })
      .catch(error => console.log("There was an error:", error))
    setParsing(false)
  }
  //PARSE_ALL
  async function parseAll(){
    setParsing(true)
    await fetch(`http://161.35.206.91:8080/all_parse/`,{
      method:"POST",
      headers:{ "Content-Type":"application/json", Authorization: "Token " + window.localStorage.getItem("amazon_auth_token")},
      body:JSON.stringify()
    })
      .then(response => {
        if(!response.ok){
          const data = response.json()
          const error = (data && data.message) || response.status
          return Promise.reject(error)
        }
      })
      .catch(error => console.log("There was an error:", error))
    setParsing(false)
  }

  //PARSING_RESULT
  async function showResultOfParsing(productId){
    setParsing(true)
    await fetch(`http://161.35.206.91:8080/results/${productId}/`,{
      method:"GET",
      headers:{ "Content-Type":"application/json", Authorization: "Token " + window.localStorage.getItem("amazon_auth_token")},
    })
      .then(response => {
        if(!response.ok){
          const data = response.json()
          const error = (data && data.message) || response.status
          return Promise.reject(error)
        }
        return response.json()
      })
      .then(data => setParsingResults(data))
      .catch(error => console.log("There was an error:", error))
    setParsing(false)
  }

  //TABLE
  const fields = [
    { key: 'title',_style:{width: "75%"}, label: 'Title' },
    { key: 'status', label:'Status'},
    { key: 'created_date',_style:{width: "5%"}, label: 'Created date'},
    { key: 'updated_date',_style:{width: "5%"}, label: 'Updated date'},
    { key: 'actions', _style:{width: "10%"},label:''},
  ]

  //STATUS
  const getBadge = (status)=>{
    switch (status) {
      case 'parsed': return 'success'
      case 'imported': return 'secondary'
      case 'edited': return 'warning'
      case 'Banned': return 'danger'
      default: return 'primary'
    }
  }

  console.log("input value:", inputValue, "selectedProduct: ", selectedProduct)

  return (
      <CCol>
        <CCard className={'main-wrapper'}>
          <CRow className={"justify-content-between align-items-center my-2"}>
            <CCol className={"col-8"}>
              <CInput value={title || ""} onChange={(e) => dispatch(searchSuccess(e.target.value))} placeholder={"Search title"}/>
            </CCol>
            <CCol className={"col-4 d-flex justify-content-end"}>
              <CButton  className={"btn btn-info mr-1"} onClick={() => parseAll()}>Parse all</CButton>
            </CCol>
          </CRow>
          {
            loading ? <FullSpinner/> :
          <CDataTable
            items={listItems}
            fields={fields}
            itemsPerPage={10}
            hover
            sorter
            pagination
            scopedSlots = {{
              'title':(item, index)=>(<>{ selectedProduct === item.id ? (
                <td>
                <CTextarea  value={inputValue} onChange={e => setInputValue(e.target.value)} onBlur={() => updateProductItem(item.id)}/></td>
              ): ( <td>    <CTextarea  value={item.title} onFocus={() => {setSelectedProduct(item.id); setInputValue(item.title)}}/>

              </td>)}</>),
              // 'title':(item, index)=>(<td><CTextarea  value={item.title} onCLick={() => { setSelectedProduct(item.id); setInputValue(item.title)}} onFocus={() => setSelectedProduct(item.id)}/></td>),
              'status':(item, index) => (<td key={item.id}><CBadge color={getBadge(item.status)}>
                <span className={"text-capitalize"}>{item.status}</span>
              </CBadge></td>),
              'created_date':(item, index) => (<td key={item.id} className={""}><span style={{fontSize:"12px"}}>{ formatDate(item.created_at)}</span></td>),
              'updated_date':(item, index) => (<td key={item.id} className={""}><span style={{fontSize:"12px"}}>{formatDate(item.updated_at)}</span></td>),
              'actions': (item, index) => (
                <td>
                        <CRow className="m-width d-flex flex-nowrap align-items-center mx-0">
                          <a href={item.url}>
                  <CIcon role={'button'} size={'xl'} className={'text-primary mr-1'} name={'cilLink'}/></a>
                  <CIcon role={'button'} size={'xl'} className={'text-danger mr-1'} name={'cilTrash'} onClick={() => deleteProductItem(item.id)}/>
                   <CButton key={item.id}  className={"btn btn-info mr-1"} onClick={() => parseProductItem(item.id)}>Parse</CButton>
                    <CButton  className={"btn btn-success mr-1"} onClick={() => {
                      setSelectedProduct(item.id)
                      showResultOfParsing(item.id)
                      onToggle()
                    }}
                              disabled={item.status === "parsing"}>{item.status === "parsing" ? "Parsing.." :" Result"}</CButton>
                  </CRow>
                </td>
              )}}
          />}
        </CCard>

     <ProductParsingResults onToggle={onToggle}  isOpen={isOpen} selectedProduct={selectedProduct} parsingResults={parsingResults} />

      </CCol>
  )
}


//
// <CCol className={"mt-2"}>
//   <CCard className={'main-wrapper'}>
//     <CDataTable
//       items={listItems}
//       fields={fields}
//       footer
//       itemsPerPage={10}
//       hover
//       sorter
//       pagination
//       scopedSlots = {{
//         'id': (item, index) => <td key={item.id}>{index}</td>,
//         //    'title':(item, index)=>(<td onClick={() =>  {
//         //      setActiveIndex(item.id)
//         //
//         //      setInputValue(item.title || "")}}>
//         //      { activeIndex === item.id ? <CTextarea  value={inputValue} onChange={e => setInputValue(e.target.value)} onBlur={() => updateProductItem(item.id)}/>: <h6 >{item.title}</h6>}
//         // </td>),
//         'title':(item, index)=>(<td>
//           <CTextarea  value={item.title} onChange={e => setInputValue(e.target.value)} onBlur={() => updateProductItem(item.id)}/> </td>),
//         'edit':(item, index) => (<td key={item.id} className={"d-flex justify-content-center"}>
//           <CIcon role={'button'} size={'xl'} className={'row'} name={'cilFullscreen'} onClick={toggleDetails.bind(null,index)}/></td>),
//         'parse':item => <td key={item.id}>   { parsing ? <MiniSpinner/>:  <CButton  className={"btn btn-info"} onClick={() => {
//           setActiveIndex(item)
//           parseProductItem(activeIndex.item)
//         }}>Parse</CButton>}</td>,
//         'result':item => <td key={item.id}>    <CButton  className={"btn btn-success"}>Result</CButton></td>,
//         'details':
//           (item, index)=>{                          setInputValue(item.title || "")
//
//             return (
//               <CCollapse show={details.includes(index)}>
//                 <CCardBody>
//
//                   {activeIndex === item.id ? (
//                     <CTextarea value={inputValue} onChange={e => setInputValue(e.target.value)} onBlur={() => updateProductItem(item.id)}/>
//                   ) :(                         <h6>{item.title}</h6>
//                   )
//                   }
//                   <p className="text-muted">Created Date: {formatDate(item.created_at)}</p>
//                   <p className="text-muted">Updated Date: {formatDate(item.updated_at)}</p>
//
//                   <p className="text-muted">Status:    <CBadge color={getBadge(item.status)}>
//                     <span className={"text-capitalize"}>{item.status}</span>
//                   </CBadge> </p>
//                   <CButton size="sm" color="info" onClick={toggleDetails.bind(null,index)}>
//                     Close
//                   </CButton>
//                   <CButton size="sm" color="warning" className="ml-1" onClick={() => {
//                     setActiveIndex(item.id)
//                     setInputValue(item.title || "")
//                     // {'status': 'edited'}
//                   }}>
//                     Edit
//                   </CButton>
//                   <CButton size="sm" color="danger" className="ml-1" >
//                     Delete
//                   </CButton>
//                 </CCardBody>
//               </CCollapse>
//             )
//           }
//       }}
//     />
//
//   </CCard>
//
// </CCol>
