import React from 'react'
import CIcon from '@coreui/icons-react'
import { cilCloudUpload, cilSpreadsheet } from "@coreui/icons/js/free";

const _nav =  [
  {
    _tag: 'CSidebarNavItem',
    name: 'Ware',
    to: '/ware',
    icon: <CIcon name="cilSpreadsheet" customClasses="c-sidebar-nav-icon" size={'xl'}/>,
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Upload Excel',
    to: '/download-excel',
    icon: <CIcon name="cilCloudUpload" customClasses="c-sidebar-nav-icon" size={'xl'}/>,
  },
//   {
//     _tag: 'CSidebarNavItem',
//     name: 'Ebay',
//     to: '/ebay',
//     icon: <CIcon name="cibEbay" customClasses="c-sidebar-nav-icon" size={'xl'}/>,
//   },
// {
//     _tag: 'CSidebarNavItem',
//     name: 'Amazon',
//     to: '/amazon',
//     icon: <CIcon name="cibAmazon" customClasses="c-sidebar-nav-icon" size={'xl'}/>,
//   },
// {
//     _tag: 'CSidebarNavItem',
//     name: 'Walmart',
//     to: '/walmart',
//     icon: <CIcon name="cibEbay" customClasses="c-sidebar-nav-icon"/>,
//
//   },
]

export default _nav
