import React from "react";
import {
  CDataTable,
} from "@coreui/react";

import { formatDate } from "../../function/Functions";
import CIcon from "@coreui/icons-react";


const TableOfResults = ({data}) => {
  //TABLE
  const fields = [
    { key: 'title',_style:{width: "75%"}, label: 'Title' },
    { key: 'created_date',_style:{width: "5%"}, label: 'Created date'},
    { key: 'percent',_style:{width: "2%"}, label: 'Percent'},
    { key: 'quantity',_style:{width: "3%"}, label: 'Quantity'},
    { key: 'link', _style:{width: "10%"},label:''},
  ]
  return (
              <CDataTable
                items={data}
                fields={fields}
                itemsPerPage={15}
                hover
                sorter
                pagination
                scopedSlots = {{
                  'title': (item, index) => (<td>
                    <p>{item.title}</p></td>),
                  'created_date': (item, index) => (<td key={item.id} className={""}><span
                  >{formatDate(item.created_at)}</span></td>),
                  'percent': (item, index) => (<td key={item.id} className={""}><span className={"text--primary text-bold"}
                  >{item.percent} %</span></td>),
                  'quantity': (item, index) => (<td key={item.id} className={""}><span className={"text--orange text-bold"}
                  >{item.quantity}</span></td>),
                  'link': (item) => (
                    <td><a href={item.url} target={"_blank"}><CIcon role={'button'} size={'xl'} className={'text--primary mr-1'}
                                                                    name={'cilLink'}/></a></td>)
                }}/>

  )
}
export default TableOfResults
