import React from "react"
import {
  CButton,
  CModal,
  CModalBody,
  CModalFooter,
  CModalHeader,
} from "@coreui/react"
import {
  CNav,
  CNavItem,
  CNavLink,
  CTabContent,
  CTabPane,
  CTabs,
} from "@coreui/react"
import TableOfResults from "../table/TableOfResults"

const ProductParsingResults = ({ isOpen, parsingResults, onToggle }) => {

  return (
    <CModal
      show={isOpen}
      centered
      size="lg"
      onClose={onToggle}
    >
      { parsingResults &&  <>
      <CModalHeader><h5 className={"text-center text--primary"}>{parsingResults.title}</h5></CModalHeader>
        <CModalBody>
        <CTabs >
          <CNav variant="tabs" className="mt-2">
            <CNavItem>
              <CNavLink>Amazon</CNavLink>
            </CNavItem>
            <CNavItem>

              <CNavLink>Ebay</CNavLink>
        </CNavItem>
        <CNavItem>
        <CNavLink>Walmart</CNavLink>
        </CNavItem>
        </CNav>
        <CTabContent>
        <CTabPane>
        <TableOfResults data={parsingResults.amazon}/>
        </CTabPane>
        <CTabPane>
        <TableOfResults data={parsingResults.ebay}/>
        </CTabPane>
        </CTabContent>
        </CTabs>

        </CModalBody>
        <CModalFooter>
          <CButton color="secondary" onClick={onToggle}>
            Cancel
          </CButton>
        </CModalFooter>
      </>}
    </CModal>
  )
}
export default ProductParsingResults
