import { useState } from "react"
import { API } from "../api"

export default function Assistant({ go }) {
  const [msg, setMsg] = useState("")
  const [reply, setReply] = useState("")

  async function ask() {
    if (!msg) return
    const res = await fetch(`${API}/assistant?msg=${msg}`)
    const data = await res.json()
    setReply(data.reply)
  }

  return (
    <div className="screen">
      <h2>ATM Assistant</h2>

      <input
        placeholder="Ask something like 'check balance'"
        onChange={e => setMsg(e.target.value)}
      />

      <button className="btn" onClick={ask}>
        Ask
      </button>

      {reply && (
        <p style={{ marginTop: "16px", textAlign: "center" }}>
          🤖 {reply}
        </p>
      )}

      <button className="btn alt" onClick={() => go("dash")}>
        Back
      </button>
    </div>
  )
}
