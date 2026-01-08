import { API } from "../api"

export default function Withdraw({ user, setUser, go }) {
  let amount = ""

  async function withdraw() {
    if (!amount) return alert("Enter amount")

    const res = await fetch(
      `${API}/withdraw?card_number=${user.card}&amount=${amount}`,
      { method: "POST" }
    )
    const data = await res.json()

    if (data.status === "fraud_detected") {
      alert("⚠ Fraud detected! Transaction blocked.")
      return
    }

    if (data.status === "insufficient_balance") {
      alert("Insufficient balance")
      return
    }

    setUser({ ...user, balance: data.balance })
    alert("Please collect your cash")
    go("dash")
  }

  return (
    <div className="screen">
      <h2>Withdraw Cash</h2>

      <input
        placeholder="Enter amount"
        type="number"
        onChange={e => (amount = e.target.value)}
      />

      <button className="btn" onClick={withdraw}>
        Confirm Withdrawal
      </button>

      <button className="btn alt" onClick={() => go("dash")}>
        Back
      </button>
    </div>
  )
}
