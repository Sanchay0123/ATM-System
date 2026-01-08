export default function Dashboard({ user, go }) {
  return (
    <div className="screen">
      <h2>Account Balance</h2>
      <h1>₹{user.balance}</h1>

      <button className="btn" onClick={() => go("withdraw")}>
        Withdraw Cash
      </button>

      <button className="btn" onClick={() => go("deposit")}>
        Deposit Cash
      </button>

      <button className="btn alt" onClick={() => go("assistant")}>
        ATM Assistant
      </button>

      <button className="btn alt" onClick={() => go("login")}>
        Eject Card
      </button>
    </div>
  )
}
