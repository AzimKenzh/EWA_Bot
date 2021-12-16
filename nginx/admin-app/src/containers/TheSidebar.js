import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {
  CCreateElement,
  CSidebar,
  CSidebarBrand,
  CSidebarNav,
  CSidebarNavDivider,
  CSidebarNavTitle,
  CSidebarMinimizer,
  CSidebarNavDropdown,
  CSidebarNavItem,
} from '@coreui/react'

import CIcon from '@coreui/icons-react'

// sidebar nav config
import navigation from './_nav'
import {set} from "../redux/actions/settingsActions";

const TheSidebar = () => {
  const dispatch = useDispatch()
  const show = useSelector(state => state.settings.sidebarShow)

  return (
    <CSidebar
      show={show}
      onShowChange={(val) => dispatch(set(val))}
    >
      <CSidebarBrand className="d-md-down-none" to="/">
        <CIcon
          className="c-sidebar-brand-full mr-2"
          name="cib-amazon"
          height={35}
        />
        <h3 className={"c-sidebar-brand-full"}>Amazon Bot</h3>
        <CIcon
          className="c-sidebar-brand-minimized "
          name="cib-amazon"
          height={35}
        />

      </CSidebarBrand>
      <CSidebarNav>

        <CCreateElement
          items={navigation}
          components={{
            CSidebarNavDivider,
            CSidebarNavDropdown,
            CSidebarNavItem,
            CSidebarNavTitle
          }}
        />
      </CSidebarNav>
      <CSidebarMinimizer className="c-d-md-down-none"/>
    </CSidebar>
  )
}

export default React.memo(TheSidebar)
