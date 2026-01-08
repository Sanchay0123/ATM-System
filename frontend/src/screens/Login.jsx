import { API } from "../api"

export default function Login({ setUser, go }) {
  let card, pin

  async function login() {
    const r = await fetch(
      `${API}/login?card_number=${card}&pin=${pin}`,
      { method: "POST" }
    )
    const d = await r.json()
    if (!d.success) return alert("Invalid")
    setUser({ card, balance: d.balance })
    go()
  }

  return (
    <div className="screen">
      <h2>Insert Card</h2>
      <input placeholder="Card Number" onChange={e=>card=e.target.value} />
      <input type="password" placeholder="PIN" onChange={e=>pin=e.target.value} />
      <button className="btn" onClick={login}>Enter</button>
    </div>
  )
}
