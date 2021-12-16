import { useState } from 'react'

export const useModalState = ({ initialOpen = false } = {}) => {
  const [isOpen, setIsOpen] = useState(initialOpen)

  const onOpen = () => {
    setIsOpen(true)
  }

  const onClose = () => {
    setIsOpen(false)
  }

  const onToggle = () => {
    setIsOpen(!isOpen)
  }

  return { onOpen, onClose, isOpen, onToggle }
}




export const useConfirmModal = ({ initialOpen = false } = {}) => {
  const [isConfirmOpen, setIsConfirmOpen] = useState(initialOpen)

  const onConfirmOpen = () => {
    setIsConfirmOpen(true)
  }

  const onConfirmClose = () => {
    setIsConfirmOpen(false)
  }

  const onConfirmToggle = () => {
    setIsConfirmOpen(!isConfirmOpen)
  }

  return { onConfirmOpen, onConfirmClose, isConfirmOpen, onConfirmToggle }
}
