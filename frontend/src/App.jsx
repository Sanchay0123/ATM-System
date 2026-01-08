import { useState } from "react"
import ATMFrame from "./screens/ATMFrame"
import Login from "./screens/Login"
import Dashboard from "./screens/Dashboard"
import Withdraw from "./screens/Withdraw"
import Deposit from "./screens/Deposit"
import Assistant from "./screens/Assistant"

export default function App() {
  const [user, setUser] = useState(null)
  const [screen, setScreen] = useState("login")

  const go = s => setScreen(s)

  return (
    <ATMFrame>
      {screen === "login" && <Login setUser={setUser} go={()=>go("dash")} />}
      {screen === "dash" && <Dashboard user={user} go={go} />}
      {screen === "withdraw" && <Withdraw user={user} setUser={setUser} go={go} />}
      {screen === "deposit" && <Deposit user={user} setUser={setUser} go={go} />}
      {screen === "assistant" && <Assistant go={go} />}
    </ATMFrame>
  )
}
