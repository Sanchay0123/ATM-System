import { motion } from "framer-motion"

export default function ATMFrame({ children }) {
  return (
    <motion.div
      className="atm"
      initial={{ scale: 0.9, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      transition={{ duration: 0.4 }}
    >
      {children}
    </motion.div>
  )
}
