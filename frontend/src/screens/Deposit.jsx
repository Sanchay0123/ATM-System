import { API } from "../api"

export default function Deposit({ user, setUser, go }) {
  let amount = ""

  async function deposit() {
    if (!amount) return alert("Enter amount")

    const res = await fetch(
      `${API}/deposit?card_number=${user.card}&amount=${amount}`,
      { method: "POST" }
    )
    const data = await res.json()

    setUser({ ...user, balance: data.balance })
    alert("Deposit successful")
    go("dash")
  }

  return (
    <div className="screen">
      <h2>Deposit Cash</h2>

      <input
        placeholder="Enter amount"
        type="number"
        onChange={e => (amount = e.target.value)}
      />

      <button className="btn" onClick={deposit}>
        Confirm Deposit
      </button>

      <button className="btn alt" onClick={() => go("dash")}>
        Back
      </button>
    </div>
  )
}
