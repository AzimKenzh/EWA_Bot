import React from 'react'
import {
  CBadge,
  CDropdown,
  CDropdownItem,
  CDropdownMenu,
  CDropdownToggle,
  CImg
} from '@coreui/react'
import {useDispatch, useSelector} from "react-redux"
import {logout} from "../redux/actions/authActions"

const TheHeaderDropdown = () => {

  const dispatch = useDispatch()
  const user = useSelector(state => state.auth.user)

  const logoutHandler = () => dispatch(logout())

  return (
    <CDropdown
      inNav
      className="c-header-nav-items mx-2"
      direction="down"
    >
      <CDropdownToggle className="c-header-nav-link" caret={false}>
        <div className="c-avatar">
          <CImg
            src={'avatars/6.jpg'}
            className="c-avatar-img"
            alt="admin@bootstrapmaster.com"
          />
        </div>
      </CDropdownToggle>
      <CDropdownMenu className="pt-0" placement="bottom-end">
        <CDropdownItem
          header
          tag="div"
          color="light"
          className="text-center"
        >
          <strong>Account</strong>
        </CDropdownItem>
        <CDropdownItem onClick={logoutHandler}>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" className="c-icon c-icon-sm mfe-2" role="img">
            <polygon fill="var(--ci-primary-color, currentColor)"
                     points="77.155 272.034 351.75 272.034 351.75 272.033 351.75 240.034 351.75 240.033 77.155 240.033 152.208 164.98 152.208 164.98 152.208 164.979 129.58 142.353 15.899 256.033 15.9 256.034 15.899 256.034 129.58 369.715 152.208 347.088 152.208 347.087 152.208 347.087 77.155 272.034"
                     className="ci-primary"
            />
            <polygon fill="var(--ci-primary-color, currentColor)"
                     points="160 16 160 48 464 48 464 464 160 464 160 496 496 496 496 16 160 16"
                     className="ci-primary"
            />
          </svg>
          Выход
        </CDropdownItem>
      </CDropdownMenu>
    </CDropdown>
  )
}

export default TheHeaderDropdown
